from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"reqpath": ""}

@app.get("/{path}")
async def echo(path):
    return {"reqpath": path}
    