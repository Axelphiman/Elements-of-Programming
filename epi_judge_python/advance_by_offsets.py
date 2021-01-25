from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    """"steps = 0
    for i in reversed(range((len(A) - 1))):
        steps += 1
        if A[i] >= steps:
            steps = 0"""
    max_step_index = 0
    steps = current_max_step = A[max_step_index] + max_step_index
    counter = 0
    i = 1

    while steps > 0 and max_step_index < len(A):
        if A[i] + i > current_max_step:
            max_step_index = i
        steps -= 1
        if steps == 0:
            steps = current_max_step = A[max_step_index] + max_step_index
            counter += 1
        i += 1
    return steps == 0


 # Variante
 # Minimum steps
def jump(self, nums: List[int]) -> int:

    max_step_index = 0
    steps = nums[max_step_index] + max_step_index
    counter = 0
    i = 1

    while steps > 0 and i < len(nums):

        if nums[i] + i > nums[max_step_index] + max_step_index:
            max_step_index = i
        steps -= 1
        if i == len(nums) - 1:
            return counter + 1
        if steps == 0:
            counter += 1
            steps = nums[max_step_index] - i + max_step_index

        i += 1
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
