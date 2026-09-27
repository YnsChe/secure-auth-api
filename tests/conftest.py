""" Test Configuration file"""

import os
import pytest
from app.cores.rate_limit import login_limit
from fastapi.testclient import TestClient
from app.main import app


# Clean up the test database before and after each test
@pytest.fixture(autouse=True)
def clean_test_db():
    db_path = "users.db"
    if os.path.exists(db_path):
        os.remove(db_path)

    yield

    if os.path.exists(db_path):
        os.remove(db_path)


# Reset Rate limiter
@pytest.fixture
def reset_rate_limit():
    login_limit.reset()
    yield
    login_limit.reset()


# Register a user
@pytest.fixture()
def register_user():
    payload = {"username": "testuser", "password": "testpassword"}
    with TestClient(app) as client:
        client.post("/register/", json=payload)
    return payload


# Client fixture
@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client


# Bootstrap admin + user for RBAc tests
@pytest.fixture()
def bootstrap_auth():
    """Register two users: first user becomes admin, second user is a regular user."""
    with TestClient(app) as client:
        admin_resp = client.post("/register", json={"username": "admin_user", "password": "adminpass123"})
        assert admin_resp.status_code == 200, "Failed to register admin user"
        user_resp = client.post("/register", json={"username": "regular_user", "password": "userpass123"})
        assert user_resp.status_code == 200, "Failed to register regular user"

    return {
        "admin": {"username": "admin_user", "password": "adminpass123"},
        "user": {"username": "regular_user", "password": "userpass123"}
    }
