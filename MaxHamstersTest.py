import unittest
from HungryHamsters import max_hamsters


class Test(unittest.TestCase):
    def test_example_1(self):
        s = 7
        hamsters = [[1, 2], [2, 2], [3, 1]]
        result = max_hamsters(s, hamsters)
        self.assertEqual(result, 2)

    def test_example_2(self):
        s = 19
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        result = max_hamsters(s, hamsters)
        self.assertEqual(3, result)

    def test_example_3(self):
        s = 2
        hamsters = [[1, 50000], [1, 60000]]
        result = max_hamsters(s, hamsters)
        self.assertEqual(result, 1)

    def test_example(self):
        s = 12
        hamsters = [[3, 2], [8, 2], [5, 2]]
        result = max_hamsters(s, hamsters)
        self.assertEqual(2, result)


