import os
import sys
import pytest
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
@pytest.mark.score(points=2)
def test_suma_range():

    zad4 = importlib.import_module("src.zad4")
    assert hasattr(zad4, "wynik")
    assert zad4.wynik == sum(range(8, 81))