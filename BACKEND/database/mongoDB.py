from motor.motor_asyncio import AsyncIOMotorClient
import config as config
import logging

__all__ = ["getConnection", "connectMongo", "disconnectMongo"]

logger = logging.getLogger(__name__)


class MongoDataBase:
    client: AsyncIOMotorClient = None


db = MongoDataBase()


def getConnection() -> AsyncIOMotorClient:
    return db.client


async def connectMongo():
    mongoAddress = config.MONGO_ADDRESS
    db.client = AsyncIOMotorClient(mongoAddress)
    

async def disconnectMongo():
    if db.client:
        db.client.close()
    
