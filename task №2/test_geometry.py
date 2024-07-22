import unittest
from geometry_lib import Circle, Triangle, compute_area

class TestGeometry(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), 28.274333882308138)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_non_right_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())

    def test_compute_area_circle(self):
        circle = Circle(3)
        self.assertAlmostEqual(compute_area(circle), 28.274333882308138)

    def test_compute_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(compute_area(triangle), 6.0)

if __name__ == '__main__':
    unittest.main()
