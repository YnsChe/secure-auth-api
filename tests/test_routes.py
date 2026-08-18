from fastapi.testclient import TestClient
from app.main import app

def test_health():
    with TestClient(app) as client:
        resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Welcome to the Webapp."}


def test_regsiter():
    payload = {"username": "testuser", "password": "testpwd789"}
    with TestClient(app) as client:
        resp = client.post("/register/", json=payload)
    assert resp.status_code == 200
    assert resp.json() == {"username": "testuser"}

def test_short_pwd_register():
    payload = {"username": "testuser", "password": "testpwd"}
    with TestClient(app) as client:
        resp = client.post("/register/", json=payload)
    assert resp.status_code == 422