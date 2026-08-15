
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_rate_limit_blocks_after_3_requests():
    url = "/login"  # change if your actual path is different
    payload = {"username": "someone", "password": "wrong"}  # adapt to your schema

    # First 5 requests should be anything but 429 (e.g., 401 unauthorized, etc.)
    for i in range(3):
        resp = client.post(url, json=payload)
        assert resp.status_code != 429, f"request {i+1} unexpectedly hit rate limit"

    # 6th request should hit the rate limit
    resp4 = client.post(url, json=payload)
    assert resp4.status_code == 429