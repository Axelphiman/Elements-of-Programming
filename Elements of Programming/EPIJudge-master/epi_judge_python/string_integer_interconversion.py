from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    literals = '0123456789'
    negative = False
    string_array = []
    if x == 0:
        return '0'
    if x < 0:
        x = -x
        negative = True
    while x > 0:
        digit = x % 10
        x //= 10
        string_array.append(literals[digit])

    return '-' + ''.join(reversed(string_array)) if negative else ''.join(reversed(string_array))


def string_to_int(s: str) -> int:
    int_result = 0
    negative = False
    if s[0] == '-':
        negative = True
    s = s.strip('+-')
    for i in range(len(s)):
        int_result += int(s[-(i + 1)]) * 10**i
    return -int_result if negative else int_result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    string_to_int('0')
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
