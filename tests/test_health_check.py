from fastapi.testclient import TestClient

from app.main import app


def test_health_check():
    """GET / 应该返回 200 和 status: ok。"""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
