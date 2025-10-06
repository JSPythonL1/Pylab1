import subprocess
import pytest

@pytest.mark.score(points=2)
def test_kalkulator_dodawanie():
    proc = subprocess.run(
        ["python", "../src/zad6.py"],
        input="1\n2\n3\n",  # wybór opcji + dwie liczby
        text=True,
        capture_output=True
    )
    assert "5" in proc.stdout
