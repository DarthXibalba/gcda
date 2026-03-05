import pytest

from python.A_Easy.C_LinkedLists.ACC_ReverseLinkedList import *
from python.A_Easy.C_LinkedLists.AC_DataStructures import *

@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1], [1]),
        ([], []),
        (list(range(1, 11)), list(range(10, 0, -1)))
    ],
)
def test_reverse_linked_list(input_list, expected):
    head = CreateLinkedList(input_list)

    print(f"\nInput: {input_list}")
    PrettyPrintLinkedList(head)

    result = reverse_linked_list(head)

    print("Output:")
    PrettyPrintLinkedList(result)

    assert LinkedListToList(result) == expected
