from geometry_package.shape import Shape
import math


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * (self.radius**2)
