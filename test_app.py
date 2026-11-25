from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_root_returns_greeting():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_health_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_unknown_route_returns_not_found():
    response = client.get("/missing")

    assert response.status_code == 404
