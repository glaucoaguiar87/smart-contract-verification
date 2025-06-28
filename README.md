# Comparative Evaluation of Large Language Models and ESBMC-Solidity for Smart Contract Verification

This repository contains all scripts, datasets, and evaluation results used in our comparative study of LLMs (GPT-4, Gemini, Claude, Grok) versus the formal verification tool ESBMC-Solidity 7.9 for smart contract security auditing.

## 📂 Repository Structure

- `data/`: Raw contracts, ground truth labels, and result spreadsheets.
- `scripts/`: Python scripts used for contract retrieval, model execution, and metrics calculation.
- `results/`: Charts and tables with summarized evaluation metrics.
- `paper/`: Final version of the IEEE-formatted research article.

## 📊 Summary of Results

| Tool              | Recall | Precision | Accuracy |
|-------------------|--------|-----------|----------|
| GPT-4.0           | 21.6%  | 43.1%     | 69.0%    |
| Gemini 2.5        | 29.3%  | 49.3%     | 70.75%   |
| Claude 4.0        | 11.2%  | 38.2%     | 69.0%    |
| Grok 3 Beta       | 25.9%  | 50.0%     | 71.0%    |
| ESBMC 7.9         | 42.2%  | 73.1%     | 78.75%|

## 🛠 Requirements

- Python ≥ 3.10
- Pandas, requests, matplotlib
- [ESBMC-Solidity](https://github.com/esbmc/esbmc)
- API keys for LLMs
## 📜 License

MIT License

## 👨‍🔬 Authors

- Glauco Aguiar (UFAM)
- Maria Lima (UFAM)
- Matheus Catão (UFAM)
