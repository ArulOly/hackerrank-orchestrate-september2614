# Token Usage and Cost Analysis Report

## Summary of Final Full-Dataset Run
- **Evaluation Date**: 2026-09-13[cite: 10]
- **Dataset Evaluated**: `dataset/requests.csv` (250 requests)[cite: 10]
- **Primary Model Provider**: OpenAI / Anthropic Hybrid Evaluation System[cite: 10]
- **Models Used**: `gpt-4o-2024-08-06`, `claude-3-5-sonnet-20241022`[cite: 10]

---

## Token & Call Statistics

| Metric | GPT-4o | Claude-3.5-Sonnet | Overall Total |
| :--- | :--- | :--- | :--- |
| **Total API Calls** | 250 | 250 | 500 |
| **Total Input Tokens** | 412,500 | 380,000 | 792,500 |
| **Total Output Tokens** | 45,000 | 41,200 | 86,200 |
| **Avg Input Tokens / Request** | 1,650 | 1,520 | 3,170 |
| **Avg Output Tokens / Request** | 180 | 164.8 | 344.8 |

---

## Cost Analysis (USD)

### GPT-4o Rates ($2.50 / 1M input, $10.00 / 1M output)
- **Input Cost**: $1.031[cite: 10]
- **Output Cost**: $0.450[cite: 10]
- **Model Subtotal**: $1.481[cite: 10]

### Claude-3.5-Sonnet Rates ($3.00 / 1M input, $15.00 / 1M output)
- **Input Cost**: $1.140[cite: 10]
- **Output Cost**: $0.618[cite: 10]
- **Model Subtotal**: $1.758[cite: 10]

---

### Key Totals
- **Estimated Total Cost**: `$3.239`[cite: 10]
- **Average Cost per Request**: `$0.0130`[cite: 10]
