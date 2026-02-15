import requests
import pytest


def assert_success_response(res):
    assert res.status_code == 200
    return res.json()


@pytest.fixture
def brewery_ids(openbrewery_base_url):
    res = requests.get(f"{openbrewery_base_url}/v1/breweries", timeout=5)
    data = assert_success_response(res)
    return [e["id"] for e in data]


def test_list_breweries(openbrewery_base_url):
    res = requests.get(f"{openbrewery_base_url}/v1/breweries", timeout=5)
    data = assert_success_response(res)
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_brewery_by_id(openbrewery_base_url, brewery_ids):
    for obdb_id in brewery_ids[:3]:
        res = requests.get(f"{openbrewery_base_url}/v1/breweries/{obdb_id}", timeout=5)
        data = assert_success_response(res)
        assert data["id"] == obdb_id


@pytest.mark.parametrize("country", ["United States", "Ireland", "South Africa"])
def test_get_brewery_by_country(openbrewery_base_url, country):
    res = requests.get(
        f"{openbrewery_base_url}/v1/breweries",
        params={"by_country": country},
        timeout=5,
    )
    data = assert_success_response(res)
    assert isinstance(data, list)
    assert len(data) > 0
    for brewery in data:
        assert brewery["country"].lower() == country.lower()


@pytest.mark.parametrize(
    "name",
    [
        "Gordon Biersch Brewery Restaurant - San Diego",
        "Mikkeller Brewing San Diego",
        "San Diego Brewing Co",
    ],
)
def test_get_brewery_by_name(openbrewery_base_url, name):
    res = requests.get(
        f"{openbrewery_base_url}/v1/breweries", params={"by_name": name}, timeout=5
    )
    data = assert_success_response(res)
    assert isinstance(data, list)
    assert len(data) > 0
    for brewery in data:
        assert brewery["name"].lower() == name.lower()
