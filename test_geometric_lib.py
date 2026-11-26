import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertAlmostEqual(circle.area(5), math.pi * 25, places=6)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25, places=6)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-5)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5, places=6)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle.perimeter(1.5), 2 * math.pi * 1.5, places=6)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-5)


class SquareTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(square.area(5), 25)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(square.area(2.5), 6.25, places=6)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-4)

    def test_perimeter_positive(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10.0, places=6)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-4)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            square.perimeter("5")


class RectangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(rectangle.area(3, 5), 15)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_square_case(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_float(self):
        self.assertAlmostEqual(rectangle.area(2.5, 4.0), 10.0, places=6)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, 5)

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle.area("3", 5)

    def test_perimeter_positive(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(10, 0), 20)

    def test_perimeter_float(self):
        self.assertAlmostEqual(rectangle.perimeter(2.5, 3.5), 12.0, places=6)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, 5)


class TriangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(triangle.area(6, 4), 12.0)

    def test_area_zero(self):
        self.assertEqual(triangle.area(6, 0), 0.0)

    def test_area_float(self):
        self.assertAlmostEqual(triangle.area(3.5, 2.0), 3.5, places=6)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-6, 4)

    def test_perimeter_positive(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_float(self):
        self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3.0), 7.0, places=6)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)

    def test_perimeter_nonexistent_triangle(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 2, 10)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("1", "4", "5")


if __name__ == "__main__":
    unittest.main()