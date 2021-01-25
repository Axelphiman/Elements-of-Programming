from typing import List
from math import inf, isinf
from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    counter = 0
    nearest_repetition = inf
    last_seen_index = {}
    for word in paragraph:
        try:
            nearest_repetition = min(nearest_repetition, counter - last_seen_index[word])
        except KeyError:
            pass
        last_seen_index[word] = counter
        counter += 1
    return nearest_repetition if not isinf(nearest_repetition) else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
