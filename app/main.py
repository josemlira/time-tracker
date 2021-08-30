from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def health():
  return "200"