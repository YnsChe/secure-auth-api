import os
import pytest
from app.cores.rate_limit import login_limit
from fastapi.testclient import TestClient
from app.main import app

# Clean up the test database before and after each test
@pytest.fixture(scope="module",autouse=True)
def clean_test_db():
    db_path = "users.db"
    if os.path.exists(db_path):
        os.remove(db_path)

    yield

    if os.path.exists(db_path):
        os.remove(db_path)


@pytest.fixture
def reset_rate_limit():
    login_limit.reset()
    yield
    login_limit.reset()


@pytest.fixture()
def register_user():
    payload = {"username": "testuser", "password": "testpassword"}
    with TestClient(app) as client:
        client.post("/register/", json=payload)
    return payload