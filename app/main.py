from fastapi import FastAPI

from .routers import projects

app = FastAPI()


app.include_router(
  projects.router,
  prefix="/projects",
  tags=["projects"],
)

@app.get("/")
async def health() -> int:
  return 200