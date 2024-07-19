from geometry_package.shape import Shape
import math


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a: float = a
        self.b: float = b
        self.c: float = c
    
    def area(self) -> float:
        semi_perimeter: float = (self.a + self.b + self.c) / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (semi_perimeter - self.c))
    
    def is_right_triangle(self) -> bool:
        sides: list[float] = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)
