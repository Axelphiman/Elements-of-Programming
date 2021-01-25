from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test



def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    processed_inorder = {key: value for value, key in enumerate(inorder)}

    def binary_tree_from_preorder_inorder_helper():
        if not preorder:
            return None

        root = BinaryTreeNode(preorder[0])

        root_position = processed_inorder[preorder[0]]
        root.left = binary_tree_from_preorder_inorder(preorder[1: root_position + 1], inorder[: root_position])
        root.right = binary_tree_from_preorder_inorder(preorder[root_position + 1:], inorder[root_position + 1:])
        return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
