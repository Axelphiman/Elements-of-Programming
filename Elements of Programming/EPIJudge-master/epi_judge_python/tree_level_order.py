from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if tree is None:
        return []

    result = []
    nodos_nivel = deque([tree])

    while nodos_nivel:
        result.append([node.data for node in nodos_nivel])
        size = len(nodos_nivel)
        for _ in range(size):
            nodo = nodos_nivel.popleft()
            if nodo.left:
                nodos_nivel.append(nodo.left)
            if nodo.right:
                nodos_nivel.append(nodo.right)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
