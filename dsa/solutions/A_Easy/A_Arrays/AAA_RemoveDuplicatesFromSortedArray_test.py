import pytest

from python.A_Easy.A_Arrays.AAA_RemoveDuplicatesFromSortedArray import remove_duplicates_from_sorted_array
from python.pyutil.compare import assert_same_sequence

CASES = [
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ([1, 1, 1], 1, [1]),
    ([1, 2, 3], 3, [1, 2, 3]),
    ([7, 7, 7, 7, 7], 1, [7]),
    ([7], 1, [7]),
    ([-1, 0, 0, 0, 0], 2, [-1, 0]),
    ([-1, -1, -1, -1], 1, [-1]),
    ([-10, -10, -10, -9, -9, -8], 3, [-10, -9, -8]),
]

@pytest.mark.parametrize("nums,expected_length,expected_nums", CASES)
def test_remove_duplicates_from_sorted_array(nums, expected_length, expected_nums):
    assert remove_duplicates_from_sorted_array(nums) == expected_length
    assert_same_sequence(nums[:expected_length], expected_nums)
