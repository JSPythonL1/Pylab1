import os
import subprocess
import sys
import pytest
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
@pytest.mark.score(points=2)
def test_suma_range():
    proc = subprocess.run(
        ["python", "../src/zad4.py"],
        text=True,
        capture_output=True
    )
    assert "3212" in proc.stdout