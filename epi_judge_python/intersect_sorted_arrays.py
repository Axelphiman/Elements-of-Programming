from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    intersection = []
    indexA = indexB = 0
    while indexA < len(A) and indexB < len(B):
        if A[indexA] < B[indexB]:
            indexA += 1
        elif A[indexA] > B[indexB]:
            indexB += 1
        else:
            if not intersection or A[indexA] != intersection[-1]:
                intersection.append(A[indexA])
            indexA += 1
            indexB += 1
    return intersection


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
