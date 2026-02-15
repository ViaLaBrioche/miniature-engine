import requests


def test_get_ya(url, status_code):
    res = requests.get(url, timeout=5)
    assert res.status_code == status_code
