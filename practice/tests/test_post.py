from faker import Faker
from fastapi.testclient import TestClient

fake = Faker("ko_KR")


def test_create_post(client: TestClient) -> None:
    data = {"body": fake.text()}
    response = client.post("/posts/", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["body"] == data["body"]


def test_create_commnet(client: TestClient) -> None:
    data = {"body": fake.text(), "post_id": 1}
    response = client.post("/posts/1/comments", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["body"] == data["body"]
    assert content["post_id"] == 1
    assert content == data


def test_create_post_missing_data(client: TestClient) -> None:
    data = {}
    response = client.post("/posts/", json=data)

    assert response.status_code == 422
