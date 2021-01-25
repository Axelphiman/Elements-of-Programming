import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

''' deletes every b and convert every a into two d'''


def replace_and_remove(size: int, s: List[str]) -> int:
    switch_index = 0
    a_counter = 0
    final_size = 0

    for i in range(size):
        if s[i] == 'a':
            a_counter += 1
        if s[i] != 'b':
            s[switch_index] = s[i]
            switch_index += 1

    final_size = a_counter + switch_index - 1
    final_size2 = final_size
    switch_index -= 1

    while switch_index >= 0:
        if s[switch_index] != 'a':
            s[final_size] = s[switch_index]
            final_size -= 1
            switch_index -= 1
        else:
            s[final_size], s[final_size - 1] = 'd', 'd'
            final_size -= 2
            switch_index -= 1
    return final_size2 + 1


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
