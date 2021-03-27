from fastapi import FastAPI

app = FastAPI()

@app.get("/{path}")
async def echo(path):
    return {"reqpath": path}
    