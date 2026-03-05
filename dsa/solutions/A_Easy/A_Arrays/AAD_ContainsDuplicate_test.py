import pytest

from python.A_Easy.A_Arrays.AAD_ContainsDuplicate import *

CASES = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True), 
    ([], False),
    ([1], False),
    ([1, 1], True),
    ([1, 2, 2, 3, 4], True),
    ([1, 2, 3, 4, 5], False),
    ([1, 2, 3, 4, 5, 1], True),
    ([1, 2, 3, 4, 5, 6], False),
]

@pytest.mark.parametrize("nums,expected", CASES)
def test_contains_duplicate_using_dict(nums, expected):
    assert contains_duplicate_using_dict(nums) == expected

@pytest.mark.parametrize("nums,expected", CASES)
def test_contains_duplicate_using_set(nums, expected):
    assert contains_duplicate_using_set(nums) == expected

@pytest.mark.parametrize("nums,expected", CASES)
def test_contains_duplicate_sort(nums, expected):
    assert contains_duplicate_sort(nums) == expected

@pytest.mark.parametrize("nums,expected", CASES)
def test_contains_duplicate_stream(nums, expected):
    assert contains_duplicate_stream(nums) == expected

@pytest.mark.parametrize("nums,expected", CASES)
def test_contains_duplicate_bitset(nums, expected):
    try:
        assert contains_duplicate_bitset(nums, max(nums)) == expected
    except ValueError:
        pass