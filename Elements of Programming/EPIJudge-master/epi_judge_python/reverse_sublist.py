from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy_head = ListNode(0, L)
    head = dummy_head

    for _ in range(1, start):
        head = head.next

    current_tail = head.next
    for _ in range(finish - start):
        current_head = current_tail.next
        current_tail.next, current_head.next, head.next = current_head.next, head.next, current_head
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
