import pytest

from python.A_Easy.C_LinkedLists.AC_DataStructures import *
from python.A_Easy.C_LinkedLists.ACA_DeleteNodeInALinkedList import *

CASES = [
    ([1, 2, 3, 4, 5], 1, [1, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 2, [1, 2, 4, 5]),
    ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 1, [10, 30, 40, 50, 60, 70, 80, 90, 100]),
    ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 2, [10, 20, 40, 50, 60, 70, 80, 90, 100]),
    ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 5, [10, 20, 30, 40, 50, 70, 80, 90, 100]),
    ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 8, [10, 20, 30, 40, 50, 60, 70, 80, 100]),
]


@pytest.mark.parametrize("input_list,idx,expected_list", CASES, ids=[
    "delete_second_node",
    "delete_third_node",
    "delete_second_of_ten",
    "delete_third_of_ten",
    "delete_sixth_of_ten",
    "delete_ninth_of_ten",
])
def test_delete_node_in_a_linked_list(input_list: list[int], idx: int, expected_list: list[int]):
    head = CreateLinkedList(input_list)

    print(f"\nInput: {input_list}, delete_idx={idx}")
    PrettyPrintLinkedList(head)

    # locate node to delete (advance idx steps from head)
    node = head
    for _ in range(idx):
        node = node.next

    print("Node to delete:")
    PrettyPrintLinkedList(node)
    print("----")

    delete_node_in_a_linked_list(node)

    print("Output:")
    PrettyPrintLinkedList(head)

    out = LinkedListToList(head)
    assert out == expected_list