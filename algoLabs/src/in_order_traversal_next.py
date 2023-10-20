"""
the file with the implementation of the task
"""


class BinaryTree:
    """
    A binary tree node class.
    """

    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def in_order_traversal_next(node: BinaryTree):
    """
    :param node:
    :return: the next element in the in-order traversal of the tree
    """
    if node is None:
        return None
    if node.parent and node.parent.left == node and not node.right:
        return node.parent
    if node.right:
        node = node.right
        while node.left is not None:
            node = node.left
        return node
    temp = node
    while node.parent and temp > node.parent:
        node = node.parent
    return node.parent
