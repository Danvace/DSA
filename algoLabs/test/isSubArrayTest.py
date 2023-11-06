import unittest
from algoLabs.src.algorithms import is_subarray

nums_1 = [1, 2, 3, 4]
nums_2 = [1, 2, 3, 4]
nums_3 = [1, 2, 3, 4, 5]


class Test(unittest.TestCase):

    def test_1(self):
        sub = [1, 2, 3]
        self.assertEqual(True, is_subarray(sub, nums_1))

    def test_2(self):
        sub = [4, 2]
        self.assertEqual(False, is_subarray(sub, nums_2))

    def test_3(self):
        sub = [1, 3, 5]
        self.assertEqual(True, is_subarray(sub, nums_3))