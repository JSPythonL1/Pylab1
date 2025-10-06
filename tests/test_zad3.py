import subprocess
import pytest

@pytest.mark.score(points=2)
def test_suma_jako_float():
    proc = subprocess.run(
        ["python", "../src/zad3.py"],
        input="2 3\n",
        text=True,
        capture_output=True
    )
    assert "5.0" in proc.stdout
