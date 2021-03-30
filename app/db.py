import sqlalchemy
import os
import random
from sqlalchemy import *
from app.models import Preset
from os import path

# https://docs.sqlalchemy.org/en/14/core/tutorial.html

class DB:
    def __init__(self, path=""):
        engine = sqlalchemy.create_engine(f"sqlite+pysqlite:///{path}", echo=True, future=True)
        with engine.begin() as conn:
            table = Table()

            # result = conn.execute(text(""))
            # print(result.all())

    def generateID():
        while True:
            randID = random.randint(0, 2**16)
            if not checkIfIDExists(randID):
                break

    def checkIfIDExists(randID: int):
        pass

    def getPresets():
        pass

    def getPreset(presetID: int):
        pass

    def createPreset():
        pass

    def updatePreset(presetID: int):
        pass

    def deletePreset(presetID: int):
        pass


if __name__ == "__main__":
    # initConn("")
    generateID()
    preset1 = Preset()