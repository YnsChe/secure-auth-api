""" Basic test for Tokens"""

def test_valid_token(client, register_user):
    login = client.post("/login/", json=register_user)
    token = login.json()["access_token"]

    resp = client.get("/user/me", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200

def test_missing_token(client):
    resp = client.get("/user/me")
    assert resp.status_code == 401

def test_invalid_token(client):
    resp = client.get("/user/me", headers={"Authorization": "Bearer this-is-not-a-valid-token"})
    assert resp.status_code == 401

