from fastapi.testclient import TestClient
from freezegun import freeze_time
import pydash as py_

from app.main import app

test_client = TestClient(app)


def test_report_all_projects():
  """
  Start a new project and create 2 segments: 5 mins / 15 mins
  Start tracking on another project but never finish it
  Then, print the report for all projects
  """
  first_project = "proj1"
  second_project = "proj2"

  # Start proj1
  with freeze_time("2021-06-01 00:00:00"):
    response = test_client.post(f"/projects/{first_project}/start")
    assert response.status_code == 200
  
  # Stop proj1
  with freeze_time("2021-06-01 00:05:01"):
    response = test_client.post(f"/projects/{first_project}/stop")
    assert response.status_code == 200
  
  # Start proj2
  with freeze_time("2021-06-01 00:06:00"):
    response = test_client.post(f"/projects/{second_project}/start")
    assert response.status_code == 200
  
  # Start proj1
  with freeze_time("2021-06-01 00:10:00"):
    response = test_client.post(f"/projects/{first_project}/start")
    assert response.status_code == 200
  
  # Stop proj1
  with freeze_time("2021-06-01 00:25:01"):
    response = test_client.post(f"/projects/{first_project}/stop")
    assert response.status_code == 200
  
  # Get report for all projects
  response = test_client.get("/projects")
  assert response.status_code == 200

  # Check first project has total_time = 20 mins
  project = py_.find(response.json(), {"project_id": first_project})
  assert project["total_time"] == 20
