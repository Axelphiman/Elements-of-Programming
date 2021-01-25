from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    literals = '0123456789ABCDEF'
    n = 0
    negative = False

    if num_as_string[0] == '-':
        negative = True
    num_as_string = num_as_string.strip('+-')
    for digits in num_as_string:
        n *= b1
        n += literals.index(digits)

    string_result = ''
    if n == 0:
        return '0'
    while n > 0:
        digit = n % b2
        n //= b2
        string_result = literals[digit] + string_result
    return '-' + string_result if negative else string_result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
