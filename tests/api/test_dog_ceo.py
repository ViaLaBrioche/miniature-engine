import requests
import pytest


def assert_success_response(res):
    assert res.status_code == 200
    data = res.json()
    assert "message" in data
    assert data["status"] == "success"
    return data


def test_get_list_all_dogs(dog_base_url):
    res = requests.get(f"{dog_base_url}/breeds/list/all", timeout=5)
    data = assert_success_response(res)
    assert isinstance(data["message"], dict)
    assert len(data["message"]) > 0


def test_get_random_image(dog_base_url):
    res = requests.get(f"{dog_base_url}/breeds/image/random", timeout=5)
    data = assert_success_response(res)
    assert isinstance(data["message"], str)


@pytest.mark.parametrize(
    "count",
    [
        pytest.param(1, id="min 1"),
        pytest.param(49, id="49"),
        pytest.param(50, id="max 50"),
    ],
)
def test_get_random_images_count(dog_base_url, count):
    res = requests.get(f"{dog_base_url}/breeds/image/random/{count}", timeout=5)
    data = assert_success_response(res)
    assert isinstance(data["message"], list)
    actual = len(data["message"])
    assert actual == count, f"{actual} не равен {count}"


@pytest.mark.parametrize(
    "breed",
    [
        pytest.param("hound", id="hound"),
        pytest.param("dachshund", id="dachshund"),
        pytest.param("akita", id="akita"),
        pytest.param("rottweiler", id="rottweiler"),
        pytest.param("beagle", id="beagle"),
    ],
)
def test_get_images_by_breed(dog_base_url, breed):
    res = requests.get(f"{dog_base_url}/breed/{breed}/images", timeout=5)
    data = assert_success_response(res)
    assert isinstance(data["message"], list)
    assert len(data["message"]) > 0
    for url in data["message"]:
        assert isinstance(url, str)
        assert breed in url


@pytest.mark.parametrize(
    "breed, subbreed",
    [
        ("hound", "afghan"),
        ("wolfhound", "irish"),
        ("segugio", "italian"),
    ],
)
def test_get_images_by_sub_breed(dog_base_url, breed, subbreed):
    res = requests.get(f"{dog_base_url}/breed/{breed}/{subbreed}/images", timeout=5)
    data = assert_success_response(res)
    assert isinstance(data["message"], list)
    for url in data["message"]:
        assert isinstance(url, str)
    assert f"{breed}-{subbreed}" in url
