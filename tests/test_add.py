"""
Testing addition in calculator.
"""
from calculator import add

def test_two_plus_two():
    """
    If the number 2 is given as a param, 4 should be returned.
    """
    assert add(2, 2) == 4
