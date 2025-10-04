import subprocess
import pytest
from datetime import date

@pytest.mark.score(points=2)
def test_roznica_dat():
    today = date.today()
    proc = subprocess.run(
        ["python", "src/zad5.py"],
        input="2000-01-01\n",
        text=True,
        capture_output=True
    )
    assert str(today.year) in proc.stdout or str(today.year - 2000) in proc.stdout
