import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    len0, len1 = 0, 0
    list_index1, list_index2 = l0, l1
    while list_index1:
        list_index1 = list_index1.next
        len0 += 1
    while list_index2:
        list_index2 = list_index2.next
        len1 += 1
    list_index1, list_index2 = l0, l1
    if len1 - len0 > 0:
        for i in range(len1 - len0):
            if list_index2:
                list_index2 = list_index2.next
    else:
        for i in range(len0 - len1):
            if list_index1:
                list_index1 = list_index1.next
    while list_index1 and list_index2:
        if list_index1 is list_index2:
            return list_index1
        list_index1 = list_index1.next
        list_index2 = list_index2.next
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
