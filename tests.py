import importlib
import subprocess
from datetime import date
import pytest

@pytest.mark.score(points=2)
def test_powitanie():
    proc = subprocess.run(
        ["python", "src/zad2.py"],
        input="Ala\n",
        text=True,
        capture_output=True
    )
    assert "Ala" in proc.stdout

@pytest.mark.score(points=2)
def test_suma_jako_float():
    proc = subprocess.run(
        ["python", "src/zad3.py"],
        input="2 3\n",
        text=True,
        capture_output=True
    )
    assert "5.0" in proc.stdout

@pytest.mark.score(points=2)
def test_suma_range():
    zad4 = importlib.import_module("src/zad4")
    assert hasattr(zad4, "wynik")
    assert zad4.wynik == sum(range(8, 81))

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

@pytest.mark.score(points=2)
def test_kalkulator_dodawanie():
    proc = subprocess.run(
        ["python", "src/zad6.py"],
        input="1\n2\n3\n",  # wybór opcji + dwie liczby
        text=True,
        capture_output=True
    )
    assert "5" in proc.stdout


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    total_score = 0
    max_score = 0
    for result in terminalreporter.stats.get('passed', []) + terminalreporter.stats.get('failed', []):
        score = getattr(result, 'score', 0)
        max_pts = getattr(result, 'max_score', 0)
        total_score += score
        max_score += max_pts
    terminalreporter.write_sep("-", f"Wynik końcowy: {total_score}/{max_score} punktów")

def pytest_runtest_makereport(item, call):
    if "score" in item.keywords and call.when == "call":
        outcome = call.excinfo is None
        score = item.get_closest_marker("score").kwargs.get("points", 0)
        item.score = score if outcome else 0
        item.max_score = score
