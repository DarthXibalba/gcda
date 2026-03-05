import pytest

from python.A_Easy.B_Strings.ABA_ReverseString import reverse_string
from python.pyutil.compare import assert_same_sequence

CASES = [
    (["h","e","l","l","o"], ["o","l","l","e","h"]),
    (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]),
    (["I"], ["I"]),
]

@pytest.mark.parametrize("s,expected", CASES)
def test_reverse_string(s: str, expected: str):
    reverse_string(s)
    assert_same_sequence(s, expected)
