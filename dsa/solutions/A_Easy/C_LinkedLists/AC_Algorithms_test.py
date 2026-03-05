import pytest

from python.A_Easy.C_LinkedLists.AC_Algorithms import *
from python.A_Easy.C_LinkedLists.AC_DataStructures import *

@pytest.mark.parametrize(
    "input_list, midpoint, expected",
    [
        ([1, 2, 3, 4, 5], 3, [3, 4, 5]),
        ([1, 2, 3, 4], 3, [3, 4]),
        ([1], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 2, [2, 3]),
        ([1, 2, 3, 4, 5, 6], 4, [4, 5, 6]),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5]),
    ],
)

def test_fast_slow_pointer_traversal(input_list, midpoint, expected):
    head = CreateLinkedList(input_list)

    print(f"\nInput: {input_list}")
    PrettyPrintLinkedList(head)

    midpt, tail = fast_slow_pointer_traversal(head)

    print("Midpoint:")
    PrettyPrintLinkedList(midpt)

    print("Tail:")
    PrettyPrintLinkedList(tail)

    out_list = LinkedListToList(midpt)
    assert out_list == expected
