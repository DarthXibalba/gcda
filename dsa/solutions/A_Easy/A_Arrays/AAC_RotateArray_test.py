import pytest

from python.A_Easy.A_Arrays.AAC_RotateArray import rotate_array
from python.pyutil.compare import assert_same_sequence

CASES = [
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    ([-1,-100,3,99], 2, [3,99,-1,-100]),
    (["A","B","C","D","E","F","G"], 2, ["F","G","A","B","C","D","E"]),
    (["A","B","C","D","E","F","G"], 5, ["C","D","E","F","G","A","B"]),
    ([-1], 2, [-1])
]

@pytest.mark.parametrize("nums,k,expected", CASES)
def test_rotate_array(nums, k, expected):
    rotate_array(nums, k)
    assert_same_sequence(nums, expected)
