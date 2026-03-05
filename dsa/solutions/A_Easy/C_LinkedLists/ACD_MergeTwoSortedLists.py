from python.A_Easy.C_LinkedLists.AC_DataStructures import *

def merge_two_sorted_lists_1st_attempt(n1 : ListNode, n2 : ListNode) -> ListNode:
    if n1 == None:
        return n2
    if n2 == None:
        return n1
    head = n1
    comp = n2
    if n2.val < n1.val:
        head = n2
        comp = n1
    main = head
    while main.next != None and comp != None:
        if comp.val < main.next.val:
            tmp = main.next
            main.next = comp
            comp = tmp
        main = main.next
    if comp != None:
        main.next = comp
    return head


def merge_two_sorted_lists(n1: ListNode, n2: ListNode) -> ListNode:
    sentinel = ListNode(None, None)
    tail = sentinel

    while n1 != None and n2 != None:
        if n1.val <= n2.val:
            tail.next = n1
            n1 = n1.next
        else:
            tail.next = n2
            n2 = n2.next
        tail = tail.next

    if n1 != None:
        tail.next = n1

    elif n2 != None:
        tail.next =n2

    return sentinel.next
