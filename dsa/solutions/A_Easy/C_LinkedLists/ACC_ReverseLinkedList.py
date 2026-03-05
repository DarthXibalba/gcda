from python.A_Easy.C_LinkedLists.AC_DataStructures import *

def reverse_linked_list_first_attempt(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    prev = None
    cur = head
    next = head.next

    while next != None:
        cur.next = prev
        prev = cur
        cur = next
        next = next.next
    
    cur.next = prev
    return cur


def reverse_linked_list(head: ListNode) -> ListNode:
        prev = None
        cur = head

        while cur:
             next = cur.next
             cur.next = prev
             prev = cur
             cur = next

        return prev