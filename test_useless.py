import pytest
import useless
import math


@pytest.mark.parametrize('a, b, c', [
    (1, 2, -8),
    (2, 2, -16)
])
def test_useless(a, b, c):
    x1, x2 = useless.quadratic(a, b, c)
    assert math.isclose(a*x1**2 + b*x1 + c, 0)
    assert math.isclose(a*x2**2 + b*x2 + c, 0)
