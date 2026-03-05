from python.A_Easy.C_LinkedLists.AC_DataStructures import *

def remove_nth_node_from_end(head: ListNode, n: int) -> ListNode | None:
    # If LL has only 1 element
    if head.next == None:
        return None
    # Offset curNode by n-1 jumps
    curNode = head
    for _ in range(n-1):
        curNode = curNode.next
    # Introduce nth node pointer
    nthNode = head
    prevNode = ListNode(None, head)
    # Increment all pointers until curNode is tail
    while (curNode.next != None):
        curNode = curNode.next
        nthNode = nthNode.next
        prevNode = prevNode.next
    # CurNode is now tail, remove nth. Account for case where nth is head
    if nthNode is head:
        head = head.next
    else:
        prevNode.next = nthNode.next
        nthNode = None
    return head

