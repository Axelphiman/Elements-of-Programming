from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    s = s.strip('!?.()[]{}@/><=^#$-_')
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == ' ' or s[i] == ',':
            i += 1
            continue
        if s[j] == ' ' or s[j] == ',':
            j -= 1
            continue
        if s[i].capitalize() != s[j].capitalize():
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
