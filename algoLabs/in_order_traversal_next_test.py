"""
tests for in order traversal next
"""

import unittest

from in_order_traversal_next import in_order_traversal_next, BinaryTree


class TestInOrderTraversalNext(unittest.TestCase):
    """
    A test class for the in_order_traversal_next function,
     which finds the next node in in-order traversal of a binary tree.
    """

    def test_null(self):
        """
        Test case to check if in_order_traversal_next handles a None root properly.
        """
        self.assertIsNone(in_order_traversal_next(None))

    def test_next_in_order_with_right_child(self):
        """
        Test case to verify that in_order_traversal_next correctly
         identifies the next in-order node when there's a right child.
        """
        root = BinaryTree(10)
        root.right = BinaryTree(20)
        next_node = in_order_traversal_next(root)
        self.assertEqual(next_node.value, 20)

    def test_next_in_order_with_no_right_child(self):
        """
        Test case to verify that in_order_traversal_next correctly returns
         None when there's no right child.
        """
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        next_node = in_order_traversal_next(root)
        self.assertEqual(next_node, None)

    def test_next_in_order_with_parent(self):
        """
        Test case to ensure that in_order_traversal_next considers
         the parent relationship when finding the next in-order node.
        """
        root = BinaryTree(10)
        left = BinaryTree(5)
        root.left = left
        left.parent = root
        next_node = in_order_traversal_next(left)
        self.assertEqual(next_node.value, 10)

    def test_next_in_order_with_no_next_node(self):
        """
        Test case to check if in_order_traversal_next
         returns None when there's no next in-order node.
        """
        root = BinaryTree(10)
        next_node = in_order_traversal_next(root)
        self.assertIsNone(next_node)


if __name__ == '__main__':
    unittest.main()
