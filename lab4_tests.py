import data
import lab4
import unittest
import math


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        def test_first_element_1(self):
            input = [[1, 2], [3, 4], [], [4, 3, 5]]
            result = lab4.first_element(input)
            expected = [1, 3, 4]
            self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinate1(self: list[data.Point]):
        points = [data.Point(7, 20), data.Point(4, 19), data.Point(1, 20)]
        result = lab4.x_coordinates(points)
        expected = [7, 4, 1]
        self.assertEqual(result, expected)

    def test_x_coordinate2(self: list[data.Point]):
        points = [data.Point(2, 3), data.Point(0, 0), data.Point(-5, 10)]
        result = lab4.x_coordinates(points)
        expected = [2, 0, -5]
        self.assertEqual(result, expected)
    # Part 3
    def test_in_positive_quadrant_1(self):
        points = [data.Point(1, 1), data.Point(-1, 2), data.Point(3, 4)]
        result = lab4.in_positive_quadrant(points)
        expected = [data.Point(1, 1), data.Point(3, 4)]
        self.assertEqual(result, expected)

    def test_in_positive_quadrant_2(self):
        points = [data.Point(0, 0), data.Point(-1, -1), data.Point(5, 5)]
        result = lab4.in_positive_quadrant(points)
        expected = [data.Point(5, 5)]
        self.assertEqual(result, expected)
    # Part 4
    def test_distance_1(self):
        p1 = data.Point(0, 0)
        p2 = data.Point(3, 4)
        result = lab4.distance(p1, p2)
        expected = 5.0  # 3-4-5 triangle
        self.assertAlmostEqual(result, expected)

    def test_distance_2(self):
        p1 = data.Point(1, 1)
        p2 = data.Point(4, 5)
        result = lab4.distance(p1, p2)
        expected = 5.0
        self.assertAlmostEqual(result, expected)
    # Part 5
    def test_manhattan_distance_1(self):
        p1 = data.Point(1, 1)
        p2 = data.Point(4, 5)
        result = lab4.manhattan_distance(p1, p2)
        expected = 7  # (4 - 1) + (5 - 1)
        self.assertAlmostEqual(result, expected)

    def test_manhattan_distance_2(self):
        p1 = data.Point(-1, -1)
        p2 = data.Point(1, 1)
        result = lab4.manhattan_distance(p1, p2)
        expected = 4
        self.assertAlmostEqual(result, expected)
    # Part 6
    def test_distance_all_1(self):
            points = [data.Point(3, 4), data.Point(1, 1), data.Point(0, 0)]
            result = lab4.distance_all(points)
            expected = [5.0, math.sqrt(2), 0.0]
            self.assertEqual(result, expected)

    def test_distance_all_2(self):
        points = [data.Point(6, 8), data.Point(2, 2)]
        result = lab4.distance_all(points)
        expected = [10.0, math.sqrt(8)]
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
