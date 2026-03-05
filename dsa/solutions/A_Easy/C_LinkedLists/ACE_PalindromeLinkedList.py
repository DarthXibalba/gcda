from python.A_Easy.C_LinkedLists.AC_DataStructures import *

def is_palindrome_1st_attempt(head: ListNode) -> bool:
    vals = []
    while head != None:
        vals.append(head.val)
        head = head.next

    i = 0
    j = len(vals) - 1
    while i < j:
        if vals[i] != vals[j]:
            return False
        i += 1
        j -= 1
    return True

# Find midpoint using fast & slow pointers
# Reverse linked list after midpoint
def is_palindrome_2nd_attempt(head: ListNode) -> bool:
    if head == None or head.next == None:
        return True

    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next
        fast = fast.next
        slow = slow.next
    midpt = slow

    # Reverse second half of the linked list
    prev = slow
    slow = slow.next
    midpt.next = None

    while slow != None:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    tail = prev

    # Traverse list from both ends
    h = head
    t = tail
    while (h is not midpt):
        if h.val != t.val:
            return False
        h = h.next
        t = t.next
    
    # Extra Credit: Reorder linked list in original order if asked
    return True

# Correctly handle the odd invariant by setting slow to be the start of the second half and not the midpoint
# Then set prev == None so that the start of the second half will point to None as its next value and we can iterate on while(t)
def is_palindrome(head: ListNode) -> bool:
    if head == None or head.next == None:
        return True

    i = head
    j = head
    while j != None and j.next != None:
        i = i.next
        j = j.next.next
    
    # Handle the odd case (j.next == None), increment slow so that it is the start of the second half and not the midpt
    if j != None:
        i = i.next
    
    # Reverse second half of linked list
    prev = None
    while i != None:
        nxt = i.next
        i.next = prev
        prev = i
        i = nxt
    # prev is now at tail

    # Traverse list until t points to None
    h = head
    t = prev
    while t != None:
        if h.val != t.val:
            return False
        h = h.next
        t = t.next
    return True
