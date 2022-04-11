import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_ADDRESS: str
    DB_NAME: str
    TABLE_TODO_LIST: str

    class Config:
        env_file = '.env'


settings = Settings()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

"""
DEFAULT KEYWORD
"""
DEFAULT = "default"
"""
DEFAULT KEYWORD
"""
MONGO_ADDRESS = settings.MONGO_ADDRESS
"""
DATABASE KEYWORD
"""
DB_NAME = settings.DB_NAME
"""
COLLECTION KEYWORD
"""
TABLE_TODO_LIST = settings.TABLE_TODO_LIST

DB_TABLE = {
    TABLE_TODO_LIST: TABLE_TODO_LIST,
}


def getMessageResponse(custom_code):
    return {
        # success messages
        '200': {"code": "200", "message": "successfully get."},
        '200_1': {"code": "200", "message": "successfully save."},
        '200_2': {"code": "200", "message": "successfully update."},
        '200_3': {"code": "200", "message": "successfully delete."},

        # not found related messages
        '404': {"code": "400", "message": "Function not found."},

        # dataframe related messages
        '500': {"code": "500", "message": "Dataframe is empty."},
        '500_1': {"code": "500", "message": "Dataframe doesn't contains selected field."},
        '500_2': {"code": "500", "message": "Bad type of data delivered."},
        '500_3': {"code": "500", "message": "Error while operation."},

    }.get(custom_code, "this code is not available in our message response directory. Please add it.")
