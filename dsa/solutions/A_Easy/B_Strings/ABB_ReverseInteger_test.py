import pytest

from python.A_Easy.B_Strings.ABB_ReverseInteger import reverse_integer

CASES = [
    (123, 321),
    (-123, -321),
    (120, 21),
    [1534236469, 0]
]

@pytest.mark.parametrize("x,expected", CASES)
def test_reverse_integer(x, expected):
    assert reverse_integer(x) == expected
