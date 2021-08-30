from dataclasses import dataclass
from functools import reduce
from typing import List


@dataclass
class Segment:
  start: str
  stop: str
  total_time: int  # Time spent in minutes

@dataclass
class Project:
  project_id: str
  segments: List[Segment]
  total_time: int  # Time spent in minutes


def render_segment(segment: dict) -> Segment:
  return Segment(
    start=str(segment["start"]),
    stop=str(segment["stop"]),
    total_time=(segment["stop"] - segment["start"]).total_seconds() // 60,  # Render minutes
  )

def render_project(project: dict) -> Project:
  # Only consider stopped segments
  segments = [render_segment(seg) for seg in project["segments"] if "stop" in seg]
  return Project(
    project_id=project["project_id"],
    segments=segments,
    total_time=reduce(lambda acc, curr: acc + curr.total_time, segments, 0),
  )