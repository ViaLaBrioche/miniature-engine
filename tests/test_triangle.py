from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, side_c, area",
    [
        (5, 6, 7, 14.7),
        (3.5, 4.2, 5.1, 7.29),
    ],
    ids=["integer", "float"],
)
def test_triangle_area_correct(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert round(t.area, 2) == area


@pytest.mark.parametrize(
    "side_a, side_b, side_c, perimeter",
    [
        (7, 6, 3, 16),
        (5.5, 8.5, 6.3, 20.3),
    ],
    ids=["integer", "float"],
)
def test_triangle_perimeter_correct(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        pytest.param(-4, 3, 2, id="side_a negative"),
        pytest.param(3, 0, 4, id="zero"),
        pytest.param(14, -8, 3, id="side_b negative"),
        pytest.param(-14, -8, -3, id="sides negative"),
    ],
)
def test_triangle_sides_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError, match="Triangle side must be positive"):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        pytest.param(1, 1, 2, id="side_a + side_b <= side_c"),
        pytest.param(3, 10, 4, id="side_a + side_c <= side_b"),
        pytest.param(14, 6, 3, id="side_c + side_b <= side_a"),
    ],
)
def test_triangle_invalid(side_a, side_b, side_c):
    with pytest.raises(ValueError, match="Invalid triangle sides"):
        Triangle(side_a, side_b, side_c)
