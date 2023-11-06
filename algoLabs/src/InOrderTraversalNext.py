class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def in_order_traversal_next(node: BinaryTree):
    if node is None:
        return None
    if node.parent and node.parent.left == node and not node.right:
        return node.parent
    if node.right:
        node = node.right
        while node.left is not None:
            node = node.left
        return node
    while node.parent and node.parent.right == node:
        node = node.parent
    return node.parent
