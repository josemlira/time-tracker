from fastapi.testclient import TestClient

from app.main import app

test_client = TestClient(app)


def test_cant_start_twice():
  response = test_client.post("/projects/abc/start")
  assert response.status_code == 200

  response = test_client.post("/projects/abc/start")
  assert response.status_code == 409

def test_cant_end_twice():
  response = test_client.post("/projects/xyz/start")
  assert response.status_code == 200

  response = test_client.post("/projects/xyz/stop")
  assert response.status_code == 200

  response = test_client.post("/projects/xyz/stop")
  assert response.status_code == 409