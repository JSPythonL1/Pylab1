import subprocess
import pytest

@pytest.mark.score(points=2)
def test_powitanie():
    proc = subprocess.run(
        ["python", "../src/zad2.py"],
        input="Ala\n",
        text=True,
        capture_output=True
    )
    assert "Ala" in proc.stdout
