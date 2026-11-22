"""Headless CPU runner executed by GitHub Actions (workflow_dispatch, timeout 10m).
No secrets are stored in this repository. Writes structured metrics.json & environment.json.
"""
import io
import json
import platform
import sys
from contextlib import redirect_stdout
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CAPTURED_METRICS = []
CAPTURED_ENV = {
    "hardware": f"CPU ({platform.machine()})",
    "runtime": f"GitHub Actions ({platform.system()} {platform.release()})",
    "pythonVersion": platform.python_version(),
    "datasetSource": "Synthetic / public test fixtures (no confidential company data)",
    "databaseSource": "None / in-memory",
    "randomSeed": "42",
}

def log_lab_environment(extra=None):
    if isinstance(extra, dict):
        CAPTURED_ENV.update(extra)
    print("[LAB_ENV_JSON]", json.dumps(CAPTURED_ENV))
    return CAPTURED_ENV

def log_lab_result(metrics):
    if isinstance(metrics, dict):
        print("[LAB_RESULT_JSON]", json.dumps(metrics))

def main():
    buf = io.StringIO()
    script_source = "# --- Cell 1: Sort blocks by vertical position (y0), then horizontal (x0) ---\nimport fitz  # PyMuPDF\n\ndef extract_paragraphs(pdf_path, vertical_threshold=5.0):\n    \"\"\"\n    Extracts text blocks and merges them if they are vertically proximal.\n    \"\"\"\n    doc = fitz.open(pdf_path)\n    paragraphs = []\n\n    for page in doc:\n        # Sort blocks by vertical position (y0), then horizontal (x0)\n        blocks = sorted(page.get_text(\"blocks\"), key=lambda b: (b[1], b[0]))\n        \n        current_para = None\n        \n        for b in blocks:\n            x0, y0, x1, y1, text, block_no, block_type = b\n            \n            # Skip non-text blocks\n            if block_type != 0: continue\n            \n            # Logic: If current_para exists AND gap between \n            # previous y1 and current y0 is small, merge.\n            if current_para and (y0 - current_para['y1'] < vertical_threshold):\n                current_para['text'] += \" \" + text.strip()\n                current_para['y1'] = max(current_para['y1'], y1)\n            else:\n                # Start new paragraph\n                if current_para: paragraphs.append(current_para)\n                current_para = {'text': text.strip(), 'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1}\n        \n        if current_para: paragraphs.append(current_para)\n    \n    return paragraphs"
    ns = {
        "__name__": "__main__",
        "log_lab_environment": log_lab_environment,
        "log_lab_result": log_lab_result,
    }
    with redirect_stdout(buf):
        exec(compile(script_source, "lab_cells.py", "exec"), ns)

    now_iso = datetime.now(timezone.utc).isoformat()
    for line in buf.getvalue().splitlines():
        if "[LAB_RESULT_JSON]" in line:
            raw = line.split("[LAB_RESULT_JSON]", 1)[1].strip()
            try:
                obj = json.loads(raw)
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        CAPTURED_METRICS.append({
                            "key": str(k)[:64],
                            "value": v if isinstance(v, (int, float)) else str(v)[:120],
                            "unit": "",
                            "baseline": None,
                            "delta": "",
                            "source": "actions",
                            "capturedAt": now_iso,
                        })
            except Exception:
                pass
        elif "[LAB_ENV_JSON]" in line:
            raw = line.split("[LAB_ENV_JSON]", 1)[1].strip()
            try:
                obj = json.loads(raw)
                if isinstance(obj, dict):
                    CAPTURED_ENV.update(obj)
            except Exception:
                pass

    metrics_path = ROOT / "metrics.json"
    existing = {}
    if metrics_path.exists():
        try:
            existing = json.loads(metrics_path.read_text(encoding="utf-8"))
        except Exception:
            existing = {}

    if CAPTURED_METRICS:
        existing["metrics"] = CAPTURED_METRICS
    elif "metrics" not in existing:
        existing["metrics"] = []
    existing["labId"] = "lab_mws0iv06_io0t"
    existing["title"] = "How to extract a paragraph from a pdf file and store its position?"
    existing["generatedAt"] = now_iso
    metrics_path.write_text(json.dumps(existing, indent=2) + "\n", encoding="utf-8")

    env_path = ROOT / "environment.json"
    env_path.write_text(json.dumps(CAPTURED_ENV, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(CAPTURED_METRICS)} metric(s) to metrics.json")

if __name__ == "__main__":
    main()
