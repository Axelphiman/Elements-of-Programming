from typing import Iterator, List
import heapq
import itertools
from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    max_heap = [element for element in itertools.islice(sequence, k)]
    heapq.heapify(max_heap)
    sorted_sequence = []
    for element in sequence:
        sorted_sequence.append(heapq.heappushpop(max_heap, element))
    while max_heap:
        sorted_sequence.append(heapq.heappop(max_heap))
    return sorted_sequence


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
