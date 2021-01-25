from typing import List
import heapq
import itertools

from test_framework import generic_test
# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.

""" min_heap = []
    for i in range(k):
        min_heap.append(A[i])
    heapq.heapify(min_heap)
    for i in range(k, len(A)):
        heapq.heappushpop(min_heap, A[i])
    return heapq.heappop(min_heap)"""

def find_kth_largest(k: int, A: List[int]) -> int:
    for i in range(len(A)):






















f __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
