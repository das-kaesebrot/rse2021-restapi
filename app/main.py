from fastapi import FastAPI, Header, Response, status, HTTPException
from os import path
from app.errMessages import errorMsg
from app.token import checkToken
import app.db as dbhandler


version: int = 1
basepath: str = path.join("/", "evi", "api", f"v{version}")
presetspath: str = "presets"

tags_metadata = [
    {
        "name": "presets",
        "description": "Preset-specific operations. Requires authentication via _X-Auth-Token_ Header.",
    }
]
app = FastAPI(
    title="RESTful EVI API",
    description="Example implementation of a RESTful API for updating presets on an EVI system",
    version=version,
    redoc_url=None,
    openapi_tags=tags_metadata
)

db = dbhandler.DB()



# Get all presets
@app.get(path.join(basepath, presetspath), summary="getPresets()", tags=["presets"])
async def getPresets(response: Response, x_auth_token: str = Header(None)):
    """
    Gets all presets on the server.
    """
    if not checkToken(x_auth_token):
        raise HTTPException(status_code=401, detail=errorMsg.Info_FalseToken)
    
    return db.getPresets()



# Create a preset
@app.post(path.join(basepath, presetspath), summary="createPreset()", status_code=201, tags=["presets"])
async def createPreset(response: Response, x_auth_token: str = Header(None)):
    """
    Creates a new preset.
    """
    if not checkToken(x_auth_token):
        raise HTTPException(status_code=401, detail=errorMsg.Info_FalseToken)



# Get properties of a specific preset
@app.get(path.join(basepath, presetspath, "{presetID}"), summary="getPreset(int presetID)", tags=["presets"])
async def getPreset(presetID: int, response: Response, x_auth_token: str = Header(None)):
    """
    Get the properties of a specific preset.
    """
    if not checkToken(x_auth_token):
        raise HTTPException(status_code=401, detail=errorMsg.Info_FalseToken)

    return {"presetID": presetID}



# Update a selected preset
@app.put(path.join(basepath, presetspath, "{presetID}"), summary="updatePreset(int presetID)", tags=["presets"])
async def updatePreset(presetID: int, response: Response, x_auth_token: str = Header(None)):
    """
    Updates a specific preset.
    """
    if not checkToken(x_auth_token):
        raise HTTPException(status_code=401, detail=errorMsg.Info_FalseToken)



# Delete a selected preset
@app.delete(path.join(basepath, presetspath, "{presetID}"), summary="deletePreset(int presetID)", status_code=204, tags=["presets"])
async def deletePreset(presetID: int, response: Response, x_auth_token: str = Header(None)):
    """
    Deletes a specific preset.
    """
    if not checkToken(x_auth_token):
        raise HTTPException(status_code=401, detail=errorMsg.Info_FalseToken)
    