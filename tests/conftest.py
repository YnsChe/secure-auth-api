import os
import pytest
from app.cores.rate_limit import login_limit

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

