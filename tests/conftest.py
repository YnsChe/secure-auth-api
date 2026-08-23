import os
import pytest


@pytest.fixture(scope="module",autouse=True)
def clean_test_db():
    db_path = "users.db"

    # Cleaning before starting
    if os.path.exists(db_path):
        os.remove(db_path)

    yield

    # Cleaning after finishing
    if os.path.exists(db_path):
        os.remove(db_path)
