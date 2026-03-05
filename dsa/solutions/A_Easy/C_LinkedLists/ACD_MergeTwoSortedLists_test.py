import pytest

from python.A_Easy.C_LinkedLists.ACD_MergeTwoSortedLists import *
from python.A_Easy.C_LinkedLists.AC_DataStructures import *

@pytest.mark.parametrize(
    "input_list1, input_list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([1], [], [1]),
        ([], [1], [1]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6]),
    ],
)
def test_merge_two_sorted_lists(input_list1, input_list2, expected):
    head1 = CreateLinkedList(input_list1)
    head2 = CreateLinkedList(input_list2)

    print(f"\nInput: {input_list1} and {input_list2}")
    PrettyPrintLinkedList(head1)
    PrettyPrintLinkedList(head2)

    result = merge_two_sorted_lists(head1, head2)

    print("Output:")
    PrettyPrintLinkedList(result)

    out_list = LinkedListToList(result)
    assert out_list == expected
