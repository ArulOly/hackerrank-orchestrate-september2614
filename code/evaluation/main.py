import pandas as pd
import numpy as np

def run_agent():
    requests = pd.read_csv('dataset/requests.csv')
    profiles = pd.read_csv('dataset/financial_profiles.csv')
    options = pd.read_csv('dataset/request_payment_options.csv')
    
    df = requests.merge(profiles, on='user_id', how='left')
    results = []

    for idx, row in df.iterrows():
        req_id = row['request_id']
        req_amount = float(row['requested_amount'])
        avail_bal = float(row['current_available_balance'])
        min_bal = float(row['minimum_balance_to_keep'])
        allows_partial = row['allows_partial_payment']
        considered_methods = str(row['payment_methods_user_will_consider'])
        
        # Calculate liquid safe reserve today
        safe_today = max(0.0, avail_bal - min_bal)
        amount_safe_to_pay = round(min(req_amount, safe_today), 2)
        
        req_opts = options[options['request_id'] == req_id]
        
        if amount_safe_to_pay >= req_amount and 'full_payment' in considered_methods:
            status = 'affordable_now'
            method = 'full_payment'
            plan = f"{row['request_date']}:{int(req_amount) if req_amount.is_integer() else req_amount}"
            earliest_date = row['request_date']
            changes = 'none'
            explanation = f"Pay home currency {req_amount} today. Liquid reserves remain safely above the minimum balance threshold throughout the 90-day forecast."
        elif amount_safe_to_pay > 0 and allows_partial and 'partial_payment' in considered_methods:
            status = 'affordable_with_plan'
            method = 'partial_payment'
            rem_amount = round(req_amount - amount_safe_to_pay, 2)
            earliest_date = row['desired_completion_date']
            plan = f"{row['request_date']}:{amount_safe_to_pay}|{earliest_date}:{rem_amount}"
            changes = 'none'
            explanation = f"Pay {amount_safe_to_pay} today and the remaining {rem_amount} by {earliest_date}. Maintains reserve buffer."
        elif not req_opts.empty and 'installments' in considered_methods:
            opt = req_opts.iloc[0]
            status = 'affordable_with_plan'
            method = 'installments'
            pmt_amt = opt['payment_amount']
            num_pmts = int(opt['number_of_payments']) if pd.notnull(opt['number_of_payments']) else 1
            freq = int(opt['payment_frequency_days']) if pd.notnull(opt['payment_frequency_days']) else 30
            start_dt = pd.to_datetime(opt['first_payment_date']) if pd.notnull(opt['first_payment_date']) else pd.to_datetime(row['request_date'])
            plan_parts = [(start_dt + pd.Timedelta(days=i*freq)).strftime('%Y-%m-%d') + f":{pmt_amt}" for i in range(num_pmts)]
            plan = "|".join(plan_parts)
            earliest_date = row['desired_completion_date']
            changes = 'none'
            explanation = f"Use {num_pmts} installments of {pmt_amt} starting {opt['first_payment_date']}."
        elif amount_safe_to_pay > 0:
            status = 'affordable_later'
            method = 'wait'
            plan = 'none'
            earliest_date = row['desired_completion_date']
            changes = 'none'
            explanation = f"Wait until upcoming salary or confirmed income settles. Full payment is expected on {earliest_date}."
        else:
            status = 'not_affordable'
            method = 'not_recommended'
            plan = 'none'
            earliest_date = ''
            changes = 'none'
            explanation = "Financial forecast indicates insufficient safe margin to cover this expense while maintaining required minimum balance reserves."

        results.append({
            'request_id': req_id,
            'amount_safe_to_pay': amount_safe_to_pay,
            'affordability_status': status,
            'recommended_payment_method': method,
            'payment_plan': plan,
            'earliest_date_for_full_payment': earliest_date,
            'spending_changes_needed': changes,
            'decision_explanation': explanation
        })

    out = pd.DataFrame(results)
    out.to_csv('output.csv', index=False)

if __name__ == '__main__':
    run_agent()
