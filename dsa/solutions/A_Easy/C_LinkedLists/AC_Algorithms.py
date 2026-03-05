from python.A_Easy.C_LinkedLists.AC_DataStructures import *

def fast_slow_pointer_traversal(head: ListNode | None) -> tuple[ListNode | None, ListNode | None]:
    fast = head
    slow = head
    # Handle both edge cases of tail or tail.next within while condition
    while fast != None and fast.next != None:
        fast = fast.next
        fast = fast.next
        slow = slow.next

    midpt = slow
    tail = fast
    return midpt, tail

def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head

    prev = None
    cur = head
    while ():
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
