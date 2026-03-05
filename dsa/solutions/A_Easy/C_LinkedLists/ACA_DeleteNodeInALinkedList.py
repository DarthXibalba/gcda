from python.A_Easy.C_LinkedLists.AC_DataStructures import *

def delete_node_in_a_linked_list(n: ListNode):
    n.val = n.next.val
    n.next = n.next.next
