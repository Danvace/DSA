import unittest

from in_order_traversal_next import in_order_traversal_next, BinaryTree


# Import your BinaryTree class and in_order_traversal_next function here

class TestInOrderTraversalNext(unittest.TestCase):

    def test_null(self):
        self.assertIsNone(in_order_traversal_next(None))

    def test_next_in_order_with_right_child(self):
        # Create a binary tree with a right child
        root = BinaryTree(10)
        root.right = BinaryTree(20)
        next_node = in_order_traversal_next(root)
        self.assertEqual(next_node.value, 20)

    def test_next_in_order_with_no_right_child(self):
        # Create a binary tree without a right child
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        next_node = in_order_traversal_next(root)
        self.assertEqual(next_node, None)

    def test_next_in_order_with_parent(self):
        # Create a binary tree with a parent node
        root = BinaryTree(10)
        left = BinaryTree(5)
        root.left = left
        left.parent = root
        next_node = in_order_traversal_next(left)
        self.assertEqual(next_node.value, 10)

    def test_next_in_order_with_no_next_node(self):
        # Create a binary tree with no next node
        root = BinaryTree(10)
        next_node = in_order_traversal_next(root)
        self.assertIsNone(next_node)


if __name__ == '__main__':
    unittest.main()
