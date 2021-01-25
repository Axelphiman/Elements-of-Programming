from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_mirror_image(left, right):
    if not left and not right:
        return True
    elif not left or not right:
        return False
    return left.data == right.data and is_mirror_image(left.left, right.right) and is_mirror_image(left.right, right.left)


def is_symmetric(tree: BinaryTreeNode) -> bool:
    return not tree or is_mirror_image(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
