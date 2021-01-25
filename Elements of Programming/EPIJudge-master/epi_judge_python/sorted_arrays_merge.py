from typing import List
import heapq
from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap = [(sorted_array[0], position, 0) for position, sorted_array in enumerate(sorted_arrays)]
    heapq.heapify(heap)
    joined_sorted_array = []
    while heap:
        element, position, inner_position = heapq.heappop(heap)
        joined_sorted_array.append(element)
        try:
            heapq.heappush(heap, (sorted_arrays[position][inner_position + 1], position, inner_position + 1))
        except IndexError:
            pass
    return joined_sorted_array



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
