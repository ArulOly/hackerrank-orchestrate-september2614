# Buy or Wait? AI Financial Affordability Agent

## System Architecture Overview
This system provides an end-to-end affordability evaluation engine combining deterministic 90-day cash-flow simulation with context resolution from user profiles, transaction logs, payment options, unstructured messages, and image extractions[cite: 8, 9].

### Data Processing & Context Resolution Pipeline
1. **Financial State Assembly**: Reads `financial_profiles.csv` for initial liquid balances and minimum balance thresholds[cite: 8, 9].
2. **Context Enrichment**: Incorporates image-extracted financial amounts and user updates from `messages.csv` to correct missing or amended financial events[cite: 8, 9].
3. **90-Day Cash-Flow Simulator**: Projects daily balances over a 90-day forecast horizon. Evaluates whether proposed payments breach minimum balance requirements[cite: 2, 8, 9].
4. **Decision Optimization Engine**: Evaluates payment paths (`full_payment`, `partial_payment`, `installments`, `wait`, `not_recommended`) against user payment preferences and ranks safe plans based on completion speed, expenditure minimization, and payment start dates[cite: 8, 9].

## Prerequisites & Installation
- **Python**: Version 3.10+ required[cite: 9, 10].
- **Dependencies**: Install required Python libraries using pip:
  ```bash
  pip install pandas numpy

Execution Instructions
Run the agent script from the repository root:

Bash
python agent.py
