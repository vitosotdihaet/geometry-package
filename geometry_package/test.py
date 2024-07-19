import unittest
import math

from geometry_package.circle import Circle
from geometry_package.triangle import Triangle
from geometry_package.shape import Shape


class TestGeometry(unittest.TestCase):

    def calculate_area(self, shape: Shape) -> float:
        return shape.area()

    def is_right_triangle(self, shape: Shape) -> bool:
        return shape.is_right_triangle()

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_right_triangle(self):
        right_triangle = Triangle(3, 4, 5)
        self.assertTrue(right_triangle.is_right_triangle())
        self.assertTrue(self.is_right_triangle(right_triangle))

        non_right_triangle = Triangle(3, 4, 6)
        self.assertFalse(non_right_triangle.is_right_triangle())
        self.assertFalse(self.is_right_triangle(non_right_triangle))

        circle = Circle(15)
        self.assertFalse(circle.is_right_triangle())
        self.assertFalse(self.is_right_triangle(circle))

    def test_calculate_area(self):
        circle = Circle(5)
        triangle = Triangle(3, 4, 5)

        self.assertAlmostEqual(circle.area(), math.pi * 25)
        self.assertAlmostEqual(self.calculate_area(circle), math.pi * 25)
        self.assertAlmostEqual(triangle.area(), 6.0)
        self.assertAlmostEqual(self.calculate_area(triangle), 6.0)


def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestGeometry)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    main()
