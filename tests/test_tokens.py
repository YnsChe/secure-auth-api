from fastapi.testclient import TestClient
from app.main import app

def test_valid_token(register_user):
    with TestClient(app) as client:
        login = client.post("/login", json=register_user)
        token = login.json()["access_token"]
        response = client.get("/user/me", headers={"Authorization": f"Bearer {token}"})

        assert response.status_code == 200

def test_missing_token():
    with TestClient(app) as client:
        response = client.get("/user/me")
    assert response.status_code == 401

def test_invalid_token():
    with TestClient(app) as client:
        response = client.get("/user/me", headers={"Authorization:": "Bearer this-is-not-a-valid-token"})
    assert response.status_code == 401

