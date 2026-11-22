# Parent-Document Retrieval: Solving the Context Fragmentation Problem

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pushkaraj007/lab-how-to-extract-a-paragraph-from-a-pdf-file-and-store-its-position/blob/main/labs/parent-document-retrieval-solving-the-context/notebook.ipynb)

## Problem Statement
Small, naive text chunks lack the holistic context required for complex financial reasoning, causing LLMs to hallucinate due to missing upstream clauses. Parent-document retrieval maps small child chunks to larger, richer parent nodes. Generic engineering direction: Implement a hierarchical retrieval system where embedding search targets child chunks, but the context fed to the LLM is the full parent document context.

**Target Success Metric:** Hallucination reduction verified via LLM-as-a-Judge against a ground-truth dataset.

## Reproducibility & Environment
- **Hardware:** GitHub Actions ubuntu-latest (2-core CPU)
- **Runtime / Python:** GitHub Actions Python 3.11 (Python 3.11)
- **Dataset Source:** Synthetic / public test fixtures (no confidential company data)
- **Database Source:** None / in-memory
- **Random Seed:** `42`

### Quick Start
```bash
pip install -r requirements.txt
pytest tests/test_solution.py
```

## Measured Results
_Run the notebook in GitHub Actions CPU or Google Colab and log metrics via `log_lab_result({...})` to populate this table._
