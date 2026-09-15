""" Basic test for Authentication"""

# Health Test
def test_health(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Welcome to the Webapp."}

# Classical Register + login test
def test_register_and_login(client):
    payload = {"username": "testuser", "password": "testpassword"}
    resp = client.post("/register/", json=payload)
    assert resp.status_code == 200
    assert resp.json() == {"username": "testuser"}

    resp = client.post("/login/", json=payload)
    assert resp.status_code == 200
    assert resp.json()["token_type"] == "bearer"

def test_short_pwd_register(client):
    payload = {"username": "testuser1", "password": "testpwd"}
    resp = client.post("/register/", json=payload)
    assert resp.status_code == 422

def test_wrong_credentials_login(client, reset_rate_limit):
    payload = {"username": "usertest", "password": "wrongpassword"}
    resp = client.post("/login/", json=payload)
    assert resp.status_code == 401

def test_duplicated_username_register(client, register_user):
    resp = client.post("/register/", json=register_user)
    assert resp.status_code == 409

# Login Teste
def test_oauth2_login(client, register_user):
    payload = {"username": "testuser", "password": "testpassword"}
    resp = client.post("/token/", data=payload)
    assert resp.status_code == 200
    assert "access_token" in resp.json()
    assert resp.json()["token_type"] == "bearer"

def test_oauth2_wrong_credentials_login(client, reset_rate_limit):
    payload = {"username": "usertest", "password": "wrongpassword"}
    resp = client.post("/token/", data=payload)
    assert resp.status_code == 401

#Rate limiter test
def test_login_rate_limit(client, register_user, reset_rate_limit):
    for _ in range(3):
        response = client.post("/login/", json=register_user)
        assert response.status_code == 200
    response = client.post("/login/", json=register_user)
    assert response.status_code == 429