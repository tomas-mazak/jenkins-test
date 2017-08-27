import math
from typing import Tuple


def quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
    """
    Compute roots of a quadratic function:

        a*x**2 + b*x + c == 0
    """
    discriminant = math.sqrt(b**2.0 - 4.0*a*c)
    x1 = (-b + discriminant) / (2.0 * a)
    x2 = (-b - discriminant) / (2.0 * a)
    return x1, x2


def add(a: float, b: float) -> float:
    """
    Add two numbers
    """
    return a + b

def mul(a: float, b: float) -> float:
    """
    Multiply two numbers
    """
    return a * b
