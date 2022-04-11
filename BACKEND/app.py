from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.mongoDB import *
from routers.todoListRouter import router as TodoListRouter
from dotenv import load_dotenv
from pathlib import Path
import os
import logging
import logging.config

# load_dotenv(dotenv_path=f".{os.getenv('DOT_ENV', 'test')}.env")
# logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
# logger = logging.getLogger(__name__)


def createApp() -> FastAPI:
    app = FastAPI()
    return app


app = createApp()

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#routers
app.include_router(TodoListRouter, prefix="/api/todo-list")


@app.on_event("startup")
async def onAppStart():
    await connectMongo()


@app.on_event("shutdown")
async def onAppShutdown():
    await disconnectMongo()
