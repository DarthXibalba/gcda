from __future__ import annotations

class ListNode:
    def __init__(self, val: int | str | None, next: ListNode | None = None):
        self.val = val
        self.next = next

def CreateLinkedList(vals: list[int] | list[str]) -> ListNode | None:
    if len(vals) == 0:
        return None
    
    head = ListNode(vals[0])
    curNode = head
    for v in vals[1:]:
        curNode.next = ListNode(v)
        curNode = curNode.next
    return head

def LinkedListToList(head: ListNode | None) -> list[int] | list[str]:
    if head == None:
        return []
    vals = []
    curNode = head
    while curNode != None:
        vals.append(curNode.val)
        curNode = curNode.next
    return vals

def PrettyPrintLinkedList(head: ListNode | None) -> None:
    vals = LinkedListToList(head)
    if not vals:
        print("None")
    else:
        print(" -> ".join(map(str, vals)) + " -> None")

