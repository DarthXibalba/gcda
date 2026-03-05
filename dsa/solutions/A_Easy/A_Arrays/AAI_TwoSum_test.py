import pytest


from python.A_Easy.A_Arrays.AAI_TwoSum import two_sum
from python.pyutil.compare import assert_same_sequence


CASES = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]


@pytest.mark.parametrize("nums,target,expected", CASES)
def test_two_sum(nums, target, expected):
    assert_same_sequence(two_sum(nums, target), expected)
