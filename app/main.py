from fastapi import FastAPI
from os import path

app = FastAPI()

version: int = 1
basepath: str = "/" + path.join("api", f"v{version}")

@app.get(basepath)
async def presets():
    return {"success": True}
    