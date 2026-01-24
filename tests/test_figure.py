from curses.textpad import rectangle

from src.figure import Figure
from src.triangle import Triangle
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
import pytest


@pytest.mark.parametrize(
    "figure, sum_area",
    [
        pytest.param(Triangle(3, 4, 5), 30),
        pytest.param(Circle(10), 338.16),
        pytest.param(Square(4), 40),
        pytest.param(Rectangle(5, 8), 64),
    ],
    ids=["Triangle", "Circle", "Square", "Rectangle"],
)
def test_triangle_add_area_figures(figure, sum_area):
    triangle = Triangle(6, 8, 10)
    assert triangle.add_area(figure) == sum_area


@pytest.mark.parametrize(
    "figure, sum_area",
    [
        pytest.param(Triangle(3, 4, 5), 320.16),
        pytest.param(Circle(10), 628.32),
        pytest.param(Square(4), 330.16),
        pytest.param(Rectangle(5, 8), 354.16),
    ],
    ids=["Triangle", "Circle", "Square", "Rectangle"],
)
def test_circle_add_area_figures(figure, sum_area):
    circle = Circle(10)
    assert circle.add_area(figure) == sum_area


@pytest.mark.parametrize(
    "figure, sum_area",
    [
        pytest.param(Triangle(3, 4, 5), 22),
        pytest.param(Circle(10), 330.16),
        pytest.param(Square(4), 32),
        pytest.param(Rectangle(5, 8), 56),
    ],
    ids=["Triangle", "Circle", "Square", "Rectangle"],
)
def test_square_add_area_figures(figure, sum_area):
    square = Square(4)
    assert square.add_area(figure) == sum_area


@pytest.mark.parametrize(
    "figure, sum_area",
    [
        pytest.param(Triangle(3, 4, 5), 30),
        pytest.param(Circle(10), 338.16),
        pytest.param(Square(4), 40),
        pytest.param(Rectangle(5, 8), 64),
    ],
    ids=["Triangle", "Circle", "Square", "Rectangle"],
)
def test_rectangle_add_area_figures(figure, sum_area):
    r = Rectangle(4, 6)
    assert r.add_area(figure) == sum_area

@pytest.mark.parametrize(
    'value',
    [
        pytest.param(30, id="integer"),
        pytest.param(34.567, id="float"),
        pytest.param('string', id="string"),
        pytest.param((1, 'test'), id="tuple"),
        pytest.param([1, 4, 'test'], id="list"),
        pytest.param({"num": 12, "str": "string"}, id="obj")

    ]
)

def test_figure_invalid(value):
    square = Square(4)
    with pytest.raises(ValueError, match="Argument must be figure"):
        square.add_area(value)
