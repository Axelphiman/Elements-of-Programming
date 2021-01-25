from test_framework import generic_test
from test_framework.test_failure import TestFailure
from list_node import ListNode


class Stack:

    def __init__(self):
        self.elements = []
        self.current_max = []

    def empty(self) -> bool:
        return not self.elements

    def max(self) -> int:
        return self.current_max[-1]

    def peek(self):
        return self.elements[-1]

    def pop(self) -> int:
        self.current_max.pop()
        return self.elements.pop()

    def push(self, x: int) -> None:
        if self.empty():
            self.current_max.append(x)
        else:
            self.current_max.append(max(x, self.max()))
        self.elements.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
