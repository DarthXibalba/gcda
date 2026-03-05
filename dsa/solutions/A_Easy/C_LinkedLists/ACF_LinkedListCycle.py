from python.A_Easy.C_LinkedLists.AC_DataStructures import *

def has_cycle(head: ListNode | None) -> bool:
    if head == None or head.next == None:
        return False

    fast = head
    slow = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return True

    return False
