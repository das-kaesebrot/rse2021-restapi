import os
import random
from app.models import Preset
from os import path

# https://docs.sqlalchemy.org/en/14/core/tutorial.html

class DB:
    def __init__(self):
        self.collection: list = []

    def generateID(self):
        while True:
            randID = random.randint(0, 2**16)
            if not self.checkIfIDExists(randID):
                return randID

    def checkIfIDExists(self, randID: int):
        for preset_ in self.collection:
            if preset_["preset"].id == randID:
                return True

    def getPresets(self):
        return self.collection


    def getPreset(self, presetID: int):
        for preset_ in self.collection:
            if preset_["preset"].id == presetID: return preset_


    def createPreset(self, data: dict):
        preset = Preset(
            id=self.generateID(),
            name=data.get("name"),
            saturation=data.get("saturation"),
            eotf=data.get("eotf"),
            colorGamut=data.get("colorGamut"),
            colorRange=data.get("colorRange")
        )
        
        if "comment" in data.keys():
            preset.comment = data.get("comment")

        self.collection.append({"preset": preset})

        return self.getPreset(preset.id)


    def updatePreset(self, presetID: int, data: dict):
        for preset_ in self.collection:
            if preset_["preset"].id == presetID:
                
                if "name" in data.keys():
                    preset_["preset"].name = data.get("name")
                
                if "saturation" in data.keys():
                    preset_["preset"].saturation = data.get("saturation")

                if "eotf" in data.keys():
                    preset_["preset"].eotf = data.get("eotf")

                if "colorGamut" in data.keys():
                    preset_["preset"].colorGamut = data.get("colorGamut")

                if "colorRange" in data.keys():
                    preset_["preset"].colorRange = data.get("colorRange")

                if "comment" in data.keys():
                    preset_["preset"].comment = data.get("comment")

                return preset_


    def deletePreset(self, presetID: int):
        for preset_ in self.collection:
            if preset_["preset"].id == presetID: self.collection.remove(preset_)


if __name__ == "__main__":
    # initConn("")
    generateID()