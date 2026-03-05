import pytest

from python.A_Easy.C_LinkedLists.AC_DataStructures import *
from python.A_Easy.C_LinkedLists.ACF_LinkedListCycle import *

@pytest.mark.parametrize(
    "input_list, cycle_index, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([1, 2, 3, 4], -1, False),
        ([1, 2, 3, 4], 2, True),
        ([1, 2, 3, 4], 3, True),
    ],
)
def test_has_cycle(input_list, cycle_index, expected):
    head = CreateLinkedList(input_list)
    if cycle_index != -1:
        tail = head
        for _ in range(len(input_list) - 1):
            tail = tail.next
        cycle_start = head
        for _ in range(cycle_index):
            cycle_start = cycle_start.next
        tail.next = cycle_start

    print(f"\nInput: {input_list} with cycle index {cycle_index}")

    result = has_cycle(head)

    print(f"Output: {result}")
    assert result == expected
