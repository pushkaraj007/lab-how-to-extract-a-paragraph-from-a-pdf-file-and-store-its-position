"""Reproducibility verification tests for structural-layout-aware-chunking-for-financial."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_metrics_manifest_valid():
    data = json.loads((ROOT / "metrics.json").read_text(encoding="utf-8"))
    assert "metrics" in data and isinstance(data["metrics"], list)
    assert "title" in data and len(data["title"]) > 0


def test_environment_manifest_valid():
    env = json.loads((ROOT / "environment.json").read_text(encoding="utf-8"))
    for field in ("hardware", "runtime", "pythonVersion", "datasetSource", "databaseSource"):
        assert field in env and isinstance(env[field], str) and len(env[field]) > 0


def test_notebook_valid_nbformat():
    nb = json.loads((ROOT / "notebook.ipynb").read_text(encoding="utf-8"))
    assert nb.get("nbformat") == 4
    assert isinstance(nb.get("cells"), list) and len(nb["cells"]) >= 1
