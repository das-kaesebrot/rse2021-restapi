from fastapi import FastAPI, Header, Response, status
from os import path
from app.errMessages import errorMsg
import uuid

app = FastAPI()

version: int = 1
basepath: str = path.join("/", "api", f"v{version}", "evi")
presetspath: str = "presets"

tokenList: list = ["test"]

# Get all presets on server
@app.get(path.join(basepath, presetspath), summary="getPresets()")
async def getPresets(response: Response):
    """
    Get all presets present on the server
    \f
    :param item: User input.
    """
    return {}

# Create a preset
@app.post(path.join(basepath, presetspath), summary="createPreset()")
async def createPreset(response: Response, x_auth_token: str = Header(None)):
    if not checkToken(x_auth_token):
        response.status_code = status.HTTP_403_FORBIDDEN
        return {
            "info": errorMsg.Info_FalseToken,
            "success": False
        }

# Get properties of a specific preset
@app.get(path.join(basepath, presetspath, "{presetID}"), summary="getPreset(presetID)")
async def getPreset(presetID: uuid.UUID, response: Response, x_auth_token: str = Header(None)):
    if not checkToken(x_auth_token):
        response.status_code = status.HTTP_403_FORBIDDEN
        return {
            "info": errorMsg.Info_FalseToken,
            "success": False
        }

    return {"presetID": presetID}

# Update a selected preset
@app.put(path.join(basepath, presetspath, "{presetID}"), summary="updatePreset(presetID)")
async def updatePreset(presetID: uuid.UUID, response: Response, x_auth_token: str = Header(None)):
    if not checkToken(x_auth_token):
        response.status_code = status.HTTP_403_FORBIDDEN
        return {
            "info": errorMsg.Info_FalseToken,
            "success": False
        }

# Delete a selected preset
@app.delete(path.join(basepath, presetspath, "{presetID}"), summary="deletePreset(presetID)")
async def deletePreset(presetID: uuid.UUID, response: Response, x_auth_token: str = Header(None)):
    if not checkToken(x_auth_token):
        response.status_code = status.HTTP_403_FORBIDDEN
        return {
            "info": errorMsg.Info_FalseToken,
            "success": False
        }

def checkToken(token: str):
    if token in tokenList:
        return True
    else:
        return False