
import pytest
from unittest import mock
from io import StringIO
import sys
import datetime

# Import student tasks
import src.zad2 as task_2
import src.zad3 as task_3
import src.zad4 as task_4
import src.zad5 as task_5
import src.zad6 as task_6

# --- Zadanie 2 ---
def test_task_2(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "Jan")
    task_2.main()
    captured = capsys.readouterr()
    assert "Jan" in captured.out

# --- Zadanie 3 ---
def test_task_3(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "1 2 3")
    task_3.main()
    captured = capsys.readouterr()
    assert float(captured.out.strip()) == 6.0

# --- Zadanie 4 ---
def test_task_4():
    result = task_4.main()
    assert result == sum(range(8, 81))

# --- Zadanie 5 ---
def test_task_5():
    days = task_5.days_since("2020-01-01")
    expected = (datetime.date.today() - datetime.date(2020, 1, 1)).days
    assert days == expected

# --- Zadanie 6 ---
def test_task_6(monkeypatch, capsys):
    inputs = iter(["1", "5", "3", "q"])  # np. dodawanie 5+3 i wyjście
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    task_6.main()
    captured = capsys.readouterr()
    assert "8" in captured.out
