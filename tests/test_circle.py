from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    "radius, area",
    [pytest.param(8, 201.06, id="integer"), pytest.param(12.6, 498.76, id="float")],
)
def test_circle_area_correct(radius, area):
    c = Circle(radius)
    assert c.area == area


@pytest.mark.parametrize(
    "radius, perimeter",
    [pytest.param(8, 50.27, id="integer"), pytest.param(12.6, 79.17, id="float")],
)
def test_circle_perimeter_correct(radius, perimeter):
    c = Circle(radius)
    assert c.perimeter == perimeter


@pytest.mark.parametrize(
    "radius", [pytest.param(0, id="zero"), pytest.param(-4, id="negative")]
)
def test_circle_radius_negative(radius):
    with pytest.raises(ValueError, match="Circle radius must be positive"):
        Circle(radius)
