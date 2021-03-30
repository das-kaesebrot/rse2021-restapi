import sqlalchemy
import os
from sqlalchemy import *
from os import path

# https://docs.sqlalchemy.org/en/14/core/tutorial.html

def initConn(dbname):
    engine = sqlalchemy.create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    with engine.begin() as conn:
        table = Table()

        # result = conn.execute(text(""))
        # print(result.all())

if __name__ == "__main__":
    initConn("")