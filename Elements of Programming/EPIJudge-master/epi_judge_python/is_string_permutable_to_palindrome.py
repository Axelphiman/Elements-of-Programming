from test_framework import generic_test
import collections

def can_form_palindrome(s: str) -> bool:
    odd_counter = 0
    counters = collections.Counter(s)
    for times in counters.values():
        if times % 2 == 1:
            odd_counter += 1
        if odd_counter > 1:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
