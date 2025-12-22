from src.figure import Figure
import math


class Circle(Figure):
    def __init__(self, circle_r: int | float):
        if circle_r <= 0:
            raise ValueError("Circle radius must be positive")
        self.circle_r = circle_r

    @property
    def area(self):
        return round(math.pi * self.circle_r**2, 2)

    @property
    def perimeter(self):
        return round(2 * (math.pi * self.circle_r), 2)
