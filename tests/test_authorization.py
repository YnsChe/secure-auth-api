""" Basic test for Authorization"""

def test_non_admin_cannot_delete_user(client, bootstrap_auth):
    resp = client.post("/login/", json=bootstrap_auth["user"])
    assert resp.status_code == 200
    token = resp.json()["access_token"]

    resp = client.delete("/user/admin_user", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 403

def test_admin_can_delete_user(client, bootstrap_auth):
    resp = client.post("/login/", json=bootstrap_auth["admin"])
    assert resp.status_code == 200
    token = resp.json()["access_token"]

    resp = client.delete("/user/regular_user", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200 # maybe 204 statt 200

def test_non_admin_cannot_call_admin_endpoint(client, bootstrap_auth):
    resp = client.post("/login/", json=bootstrap_auth["user"])
    assert resp.status_code == 200
    token = resp.json()["access_token"]

    resp = client.get("/users/", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 403
    resp = client.put("/user/admin_user/user", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 403