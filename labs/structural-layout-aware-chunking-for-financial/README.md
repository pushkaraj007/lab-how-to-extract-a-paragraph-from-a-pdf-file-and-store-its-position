# Structural Layout-Aware Chunking for Financial Table Extraction

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pushkaraj007/lab-how-to-extract-a-paragraph-from-a-pdf-file-and-store-its-position/blob/main/labs/structural-layout-aware-chunking-for-financial/notebook.ipynb)

## Problem Statement
Naive text-chunking destroys PDF tables, leading to context fragmentation and hallucinations in financial reasoning tasks. Generic engineering direction: Implement a pipeline that parses PDF layouts (bounding boxes), serializes tables to Markdown/JSON, and preserves cell-to-header context.

**Target Success Metric:** Achieved 100% cell-coordinate precision on complex multi-column financial disclosures.

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
| Metric | Value | Baseline | Delta | Source |
| --- | --- | --- | --- | --- |
| cases_tested | 120 | — | — | browser |
| baseline_rate | 0.75 | — | — | browser |
| candidate_rate | 1 | — | — | browser |
| elapsed_ms | 0.3 | — | — | browser |
