import pytest
import useless
import math


@pytest.mark.parametrize('a, b, c', [
    (1, 2, -8),
    (2, 2, -16)
])
def test_quadratic(a, b, c):
    x1, x2 = useless.quadratic(a, b, c)
    assert math.isclose(a*x1**2 + b*x1 + c, 0)
    assert math.isclose(a*x2**2 + b*x2 + c, 0)

def test_add():
    assert useless.add(1, 1) == 2

def test_mul():
    assert useless.mul(5, 5) == 25

def test_div():
    assert useless.div(9, 3) == 3
