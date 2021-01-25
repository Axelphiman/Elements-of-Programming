from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    indexA = indexB = 0

    while indexA < m:
        if A[indexA] > B[indexB]:
            A[indexA], B[indexB] = B[indexB], A[indexA]
            indexA += 1
            indexB += 1
        else:
            indexB = 0
    indexB = 0
    while indexB < n:
        A[indexA] = B[indexB]
        indexA += 1
        indexB += 1
    return A

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
