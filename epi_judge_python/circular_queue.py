from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque

class Queue:


    def __init__(self, capacity: int) -> None:
        self._data = deque()
        self._capacidad = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, x: int) -> None:
        self._data.append(x)
        self._tail += 1
        if self._tail == self._capacidad:
            self._tail = 0
        if self.tail == self._head:
            self._tail = self._capacidad
            self._capacidad *= 2

    def dequeue(self) -> int:
        self._head += 1
        return self._data.popleft()

    def size(self) -> int:
        return self._tail


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
