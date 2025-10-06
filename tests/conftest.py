import pytest

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