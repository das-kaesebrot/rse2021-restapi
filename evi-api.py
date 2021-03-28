from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"reqpath": ""}

@app.get("/api/presets")
async def presets():

    return {"reqpath": path}
    