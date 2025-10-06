import subprocess
from datetime import date, datetime

def test_roznica_dat():
    today = date.today()
    input_date = "2000-01-01"
    proc = subprocess.run(
        ["python", "../src/zad5.py"],
        input=f"{input_date}\n",
        text=True,
        capture_output=True
    )
    expected_days = (today - datetime.strptime(input_date, "%Y-%m-%d").date()).days
    assert str(expected_days) in proc.stdout
