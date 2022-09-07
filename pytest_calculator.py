import pytest

from calculator import calculator

def test_fold():
    assert calculator('2 + 2') == 4

