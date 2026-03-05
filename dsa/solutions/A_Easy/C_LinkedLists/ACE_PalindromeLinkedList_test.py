import pytest

from python.A_Easy.C_LinkedLists.ACE_PalindromeLinkedList import *
from python.A_Easy.C_LinkedLists.AC_DataStructures import *

@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], False),
        ([1, 2, 3, 4, 3, 2, 1], True),
        ([1, 2, 3, 4, 5, 4, 3, 2, 1], True),
    ],
)
def test_is_palindrome(input_list, expected):
    head = CreateLinkedList(input_list)

    print(f"\nInput: {input_list}")
    PrettyPrintLinkedList(head)

    result = is_palindrome(head)

    print(f"Output: {result}")
    assert result == expected
