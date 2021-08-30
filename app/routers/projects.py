import datetime
from typing import Dict, List

from fastapi import APIRouter, HTTPException
from tinydb import Query

from ..database import projects
from ..helpers import Project, render_project

router = APIRouter()


@router.get("/")
async def show_projects() -> List[Project]:
  """
  Report the list of projects and total time for every project
  """
  return [render_project(proj) for proj in projects.all()]

@router.get("/{project_id}")
async def show_project(project_id: str) -> Project:
  """
  Report the total time and list the individual time segments for a project
  """
  proj = projects.get(Query().project_id == project_id)
  if not proj:
    raise HTTPException(status_code=404, detail="Project not found")
  return render_project(proj)

@router.post("/{project_id}/start")
async def start_timer(project_id: str) -> Dict[str, str]:
  """
  Start the timer for a project 
  """
  proj = projects.get(Query().project_id == project_id)
  new_segment = {"start": datetime.datetime.utcnow()}
  if not proj:
    projects.insert({
      "project_id": project_id,
      "segments": [new_segment],
    })
  elif "stop" in proj["segments"][-1]:
    proj["segments"].append(new_segment)
    projects.update(proj, doc_ids=[proj.doc_id])
  else:
    raise HTTPException(status_code=409, detail="Can't start twice")
  return {"detail": "Successfully started"}

@router.post("/{project_id}/stop")
async def stop_timer(project_id: str) -> Dict[str, str]:
  """
  Stop the timer for a project 
  """
  proj = projects.get(Query().project_id == project_id)
  if not proj:
    raise HTTPException(status_code=404, detail="Can't stop an unknown project")
  last_segment = proj["segments"][-1]
  if "stop" in last_segment:
    raise HTTPException(status_code=409, detail="Can't stop twice")
  last_segment["stop"] = datetime.datetime.utcnow()
  projects.update(proj, doc_ids=[proj.doc_id])
  return {"detail": "Successfully stopped"}