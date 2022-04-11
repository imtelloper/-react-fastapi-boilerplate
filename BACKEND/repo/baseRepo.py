from database.mongoDB import *

__all__ = ["insertOne", "find", "findOne", "updateOne", "deleteOne"]


async def insertOne(database: str, collection: str, param: dict):
    return await getConnection()[database][collection].insert_one(param)


def find(database: str, collection: str):
    return getConnection()[database][collection].find()


async def findOne(database: str, collection: str, param: dict):
    return await getConnection()[database][collection].find_one(param)


async def updateOne(database: str, collection: str, param: dict, param2: dict):
    return await getConnection()[database][collection].update_one(param, param2)


async def deleteOne(database: str, collection: str, param: dict):
    return await getConnection()[database][collection].delete_one(param)