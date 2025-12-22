from src.square import Square
import pytest


@pytest.mark.parametrize(
    "side_a, area",
    [pytest.param(5, 25, id="integer"), pytest.param(6.2, 38.44, id="float")],
)
def test_square_area_correct(side_a, area):
    s = Square(side_a)
    assert round(s.area, 2) == area


@pytest.mark.parametrize(
    "side_a, perimeter",
    [pytest.param(7, 28, id="integer"), pytest.param(3.4, 13.6, id="float")],
)
def test_square_perimeter_correct(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == perimeter


@pytest.mark.parametrize(
    "side_a", [pytest.param(0, id="zero"), pytest.param(-4, id="negative")]
)
def test_square_side_negative(side_a):
    with pytest.raises(ValueError, match="Square side must be positive"):
        Square(side_a)
