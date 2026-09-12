from fastapi.testclient import TestClient
from app.main import app

def test_health():
    with TestClient(app) as client:
        resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Welcome to the Webapp."}


def test_regsiter():
    payload = {"username": "testuser", "password": "testpassword"}
    with TestClient(app) as client:
        resp = client.post("/register/", json=payload)
    assert resp.status_code == 200
    assert resp.json() == {"username": "testuser"}

def test_short_pwd_register():
    payload = {"username": "testuser1", "password": "testpwd"}
    with TestClient(app) as client:
        resp = client.post("/register/", json=payload)
    assert resp.status_code == 422

def test_duplicated_username_register():
    payload = {"username": "testuser", "password": "testpassword"}
    with TestClient(app) as client:
        resp = client.post("/register/", json=payload)
    assert resp.status_code == 409

def test_login(reset_rate_limit):
    payload = {"username": "testuser", "password": "testpassword"}
    with TestClient(app) as client:
        resp = client.post("/login/", json=payload)
    assert resp.status_code == 200

def test_wrong_credentials_login():
    payload = {"username": "usertest", "password": "wrongpassword"}
    with TestClient(app) as client:
        resp = client.post("/login/", json=payload)
    assert resp.status_code == 401

def test_oauth2_login():
    payload = {"username": "testuser", "password": "testpassword"}
    with TestClient(app) as client:
        resp = client.post("/token", data=payload)
    assert resp.status_code == 200
    assert "access_token" in resp.json()
    assert resp.json()["token_type"] == "bearer"

def test_oauth2_wrong_credentials_login(reset_rate_limit):
    payload = {"username": "usertest", "password": "wrongpassword"}
    with TestClient(app) as client:
        resp = client.post("/token", data=payload)
    assert resp.status_code == 401