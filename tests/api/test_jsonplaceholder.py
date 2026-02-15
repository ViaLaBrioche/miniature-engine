import requests
import pytest


def assert_success_response(res):
    assert res.status_code == 200
    return res.json()


def test_get_comments(jsonplaceholder_base_url):
    res = requests.get(f"{jsonplaceholder_base_url}/comments", timeout=5)
    data = assert_success_response(res)
    assert isinstance(data, list)
    assert len(data) > 0
    for o in data[:10]:
        assert o["postId"]
        assert o["id"]
        assert o["name"]
        assert o["email"]
        assert o["body"]


@pytest.mark.parametrize("post_id", [4, 5, 50, 10])
def test_get_comments_by_post_id(jsonplaceholder_base_url, post_id):
    res = requests.get(
        f"{jsonplaceholder_base_url}/posts/{post_id}/comments", timeout=5
    )
    data = assert_success_response(res)
    assert isinstance(data, list)
    assert len(data) > 0
    for o in data:
        assert o["postId"] == post_id
        assert o["id"]
        assert o["name"]
        assert o["email"]
        assert o["body"]


@pytest.mark.parametrize("post_id", [1, 50, 99, 100])
def test_get_post_by_post_id(jsonplaceholder_base_url, post_id):
    res = requests.get(f"{jsonplaceholder_base_url}/posts/{post_id}", timeout=5)
    data = assert_success_response(res)
    assert isinstance(data, dict)
    assert data["id"] == post_id

    assert "userId" in data and isinstance(data["userId"], int)
    assert "id" in data and isinstance(data["id"], int)
    assert "title" in data and isinstance(data["title"], str)
    assert "body" in data and isinstance(data["body"], str)


def test_get_photos(jsonplaceholder_base_url):
    res = requests.get(f"{jsonplaceholder_base_url}/photos", timeout=5)
    data = assert_success_response(res)
    assert isinstance(data, list)
    assert len(data) > 0
    for o in data[:10]:
        assert o["albumId"]
        assert o["id"]
        assert o["title"]
        assert o["url"]
        assert o["thumbnailUrl"]


def test_get_users(jsonplaceholder_base_url):
    res = requests.get(f"{jsonplaceholder_base_url}/users", timeout=5)
    data = assert_success_response(res)
    assert isinstance(data, list)
    assert len(data) > 0
    for o in data[:10]:
        assert o["id"]
        assert o["name"]
        assert o["username"]
        assert o["email"]
        assert o["address"]
        assert o["address"]["street"]
        assert o["address"]["suite"]
