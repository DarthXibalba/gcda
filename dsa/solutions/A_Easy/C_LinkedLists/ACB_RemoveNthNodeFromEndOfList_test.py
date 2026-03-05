import pytest

from python.A_Easy.C_LinkedLists.ACB_RemoveNthNodeFromEndOfList import *
from python.A_Easy.C_LinkedLists.AC_DataStructures import *


@pytest.mark.parametrize(
    "input_list,n,expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1, 2], 2, [2]),
        ([1, 2], 1, [1]),
        ([1], 1, []),
        (list(range(1, 6)), 5, [2, 3, 4, 5]),
        (list(range(1, 7)), 1, [1, 2, 3, 4, 5]),
        (list(range(1, 21)), 10, [*(range(1, 11)), *(range(12, 21))]),
    ],
    ids=[
        "remove_second_from_end",
        "remove_head_two_nodes",
        "remove_tail_two_nodes",
        "single_node_to_empty",
        "remove_head_five_nodes",
        "remove_last_from_six",
        "larger_list_sanity",
    ],
)
def test_remove_nth_node_from_end(input_list, n, expected):
    head = CreateLinkedList(input_list)
    print(f"\nInput: {input_list}, n={n}")
    PrettyPrintLinkedList(head)

    result = remove_nth_node_from_end(head, n)

    print("Output:")
    PrettyPrintLinkedList(result)

    out_list = LinkedListToList(result)
    assert out_list == expected
