import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def test_get_all_posts():
    response = requests.get(BASE_URL)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 100


def test_get_single_post():
    response = requests.get(f"{BASE_URL}/11")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 11
    assert data["userId"] == 2


@pytest.mark.parametrize("post_id, expected_user_id", [
    (1, 1),
    (21, 3),
    (66, 7),
    (88, 9),
    (99, 10)
])
def test_get_single_post_set(post_id, expected_user_id):
    response = requests.get(f"{BASE_URL}/{post_id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == post_id
    assert data["userId"] == expected_user_id


def test_get_incorrect_post_404():
    response = requests.get(f"{BASE_URL}/666")

    assert response.status_code == 404


def test_expected_keys():
    response = requests.get(BASE_URL)
    data = response.json()
    first_post = data[0]
    expected_keys = {"userId", "id", "title", "body"}

    assert expected_keys.issubset(first_post.keys())


def test_correct_user():
    response = requests.get(BASE_URL, params={"userId": 1})
    data = response.json()

    assert response.status_code == 200
    assert all(post["userId"] == 1 for post in data)


def test_response_time():
    response = requests.get(BASE_URL)

    assert response.elapsed.total_seconds() < 1.0


def test_create_post():
    payload = {
        "title": "ZOO",
        "body": "A monkey goes to the ZOO",
        "userId": 88
    }
    response = requests.post(BASE_URL, json=payload)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["id"] == 101


@pytest.mark.parametrize("payload", [
    {"title": "x1",
     "body": "x1",
     "userId": 1},
     {"title": "x2",
     "body": "x2",
     "userId": 16},
     {"title": "x3",
     "body": "x3",
     "userId": 44}
])
def test_create_post_set(payload):
    response = requests.post(BASE_URL, json=payload)
    data = response.json()

    assert response.status_code == 201
    for key, value in payload.items():
        assert data[key] == value
    assert "id" in data


def test_update_post():
    payload = {
        "title": "y1",
        "body": "y1",
        "userId": 99,
        "id": 1
    }
    response = requests.put(f"{BASE_URL}/1", json=payload)
    data = response.json()

    assert response.status_code == 200
    for key, value in payload.items():
        assert data[key] == value


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/1")
    data = response.json()

    assert response.status_code in [200, 204]
    assert data == {}