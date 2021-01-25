from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:

    head = ListNode()
    node_index = head

    while L1 and L2:
        if L1.data <= L2.data:
            node_index.next = L1
            node_index = node_index.next
            L1 = L1.next
        else:
            node_index.next = L2
            node_index = node_index.next
            L2 = L2.next

    node_index.next = L1 or L2
    return head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
