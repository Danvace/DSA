import copy
import unittest

from algoLabs.src.FloodFill import flood_fill


class TestFloodFill(unittest.TestCase):
    def test_basic_flood_fill(self):
        # Test Case 1: Basic test with a 3x3 matrix
        matrix1 = [
            ['A', 'A', 'A'],
            ['A', 'B', 'B'],
            ['A', 'B', 'B']
        ]
        start_x1, start_y1 = 1, 1
        target_color1 = 'B'
        replacement_color1 = 'C'
        expected_matrix1 = [
            ['A', 'A', 'A'],
            ['A', 'C', 'C'],
            ['A', 'C', 'C']
        ]
        flood_fill(matrix1, start_x1, start_y1, target_color1, replacement_color1)
        self.assertEqual(matrix1, expected_matrix1)

    def test_complex_flood_fill(self):
        # Test Case 2: Test with a 4x4 matrix
        matrix2 = [
            ['A', 'B', 'B', 'B'],
            ['A', 'A', 'B', 'B'],
            ['B', 'A', 'A', 'B'],
            ['B', 'B', 'A', 'A']
        ]
        start_x2, start_y2 = 2, 3
        target_color2 = 'A'
        replacement_color2 = 'C'
        expected_matrix2 = [
            ['A', 'B', 'B', 'B'],
            ['A', 'A', 'B', 'B'],
            ['B', 'A', 'A', 'B'],
            ['B', 'B', 'A', 'A']
        ]

        # Create a deep copy of matrix2
        matrix_copy = copy.deepcopy(matrix2)

        flood_fill(matrix_copy, start_x2, start_y2, target_color2, replacement_color2)
        self.assertEqual(expected_matrix2, matrix_copy)


if __name__ == "__main__":
    unittest.main()
