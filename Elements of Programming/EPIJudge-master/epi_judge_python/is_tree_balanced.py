from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


class UnbalancedTreeException(Exception):
    pass


def height_and_balance(node):

    if node is None:
        return True, -1
    left_balance, left_height = height_and_balance(node.left)
  #  if not left_balance:
    #     return False, -1
    right_balance, right_height = height_and_balance(node.right)
    is_balanced = left_balance and right_balance and abs(left_height - right_height) <= 1
    height = max(left_height, right_height) + 1
    return is_balanced, height


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def height_while_checking_balance(tree):
        if tree is None:
            return -1

        left_height = height_while_checking_balance(tree.left)
        right_height = height_while_checking_balance(tree.right)

        if abs(left_height - right_height) > 1:
            raise UnbalancedTreeException()

        return max(left_height, right_height) + 1

    try:
        height_while_checking_balance(tree)
    except UnbalancedTreeException:
        return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
