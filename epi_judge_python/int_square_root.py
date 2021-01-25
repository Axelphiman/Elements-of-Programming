from test_framework import generic_test


def square_root(k: int) -> int:
    left, right = 1, k
    while left <= right:
        mid = (left + right) // 2
        if mid**2 <= k < (mid + 1)**2:
            return mid
        elif mid**2 > k:
            right = mid - 1
        else:
            left = mid + 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
