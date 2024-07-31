from math_operations import add, sub, mul
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(2, 4) == 6

@pytest.mark.parametrize(
   "a, b, expected", [(2, 3, 5), (2, 4, 6)]
)
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_sub():
    assert sub(9, 8) == 1
