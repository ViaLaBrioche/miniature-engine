from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        pytest.param(7, 9, 63, id="integer"),
        pytest.param(10.5, 15.5, 162.75, id="float"),
    ],
)
def test_rectangle_area_correct(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area


@pytest.mark.parametrize(
    "side_a, side_b, perimeter",
    [
        pytest.param(7, 9, 32, id="integer"),
        pytest.param(10.5, 15.5, 52, id="float"),
    ],
)
def test_rectangle_perimeter_correct(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter


@pytest.mark.parametrize(
    "side_a, side_b",
    [
        pytest.param(10, 0, id="integer and zero"),
        pytest.param(0, 10.6, id="zero and float"),
        pytest.param(-2, 6, id="negative and positive"),
        pytest.param(-4, -8, id="negative and negative"),
    ],
)
def test_rectangle_sides_negative(side_a, side_b):
    with pytest.raises(ValueError, match="Rectangle side must be positive"):
        Rectangle(side_a, side_b)
