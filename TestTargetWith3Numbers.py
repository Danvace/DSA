from unittest import TestCase
from TargetWith3Numbers import target_with3


class Test(TestCase):
    def test_target_with_3_numbers(self):
        arr = [1, 2, 3]
        target = 6
        self.assertEqual(True, target_with3(arr, target))

    def test_target_with_3_numbers_2(self):
        arr = [1, 2, 3]
        target = 7
        self.assertEqual(False, target_with3(arr, target))

    def test_target_with_3_numbers_3(self):
        arr = [1, 2, 4]
        target = 6
        self.assertEqual(False, target_with3(arr, target))
