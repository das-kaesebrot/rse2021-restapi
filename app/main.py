from fastapi import FastAPI, Header, Response, status
from os import path
from app.errMessages import errorMsg
from app.token import checkToken
import uuid

app = FastAPI()

version: int = 1
basepath: str = path.join("/", "api", f"v{version}", "evi")
presetspath: str = "presets"

@app.get(path.join(basepath, presetspath), summary="getPresets()")
async def getPresets(response: Response, x_auth_token: str = Header(None)):
    """
    Get all presets on the server
    """
    if not checkToken(x_auth_token):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {
            "error": errorMsg.Info_FalseToken
        }
    return {}

# Create a preset
@app.post(path.join(basepath, presetspath), summary="createPreset()", status_code=201)
async def createPreset(response: Response, x_auth_token: str = Header(None)):
    if not checkToken(x_auth_token):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {
            "error": errorMsg.Info_FalseToken
        }

# Get properties of a specific preset
@app.get(path.join(basepath, presetspath, "{presetID}"), summary="getPreset(int presetID)")
async def getPreset(presetID: uuid.UUID, response: Response, x_auth_token: str = Header(None)):
    if not checkToken(x_auth_token):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {
            "error": errorMsg.Info_FalseToken
        }

    return {"presetID": presetID}

# Update a selected preset
@app.put(path.join(basepath, presetspath, "{presetID}"), summary="updatePreset(int presetID)")
async def updatePreset(presetID: uuid.UUID, response: Response, x_auth_token: str = Header(None)):
    if not checkToken(x_auth_token):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {
            "error": errorMsg.Info_FalseToken
        }

# Delete a selected preset
@app.delete(path.join(basepath, presetspath, "{presetID}"), summary="deletePreset(int presetID)")
async def deletePreset(presetID: uuid.UUID, response: Response, x_auth_token: str = Header(None)):
    if not checkToken(x_auth_token):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {
            "error": errorMsg.Info_FalseToken
        }
    