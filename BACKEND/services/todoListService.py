import config
from repo.baseRepo import *
from bson.objectid import ObjectId

__all__ = [
    "addTodo",
    "searchTodos",
    "searchTodo",
    "updateTodo",
    "removeTodo",
]


def todoListHelper(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "content": str(todo["content"]),
        "done": bool(todo["done"]),
        "date": str(todo["date"]),
    }


async def addTodo(todo) -> dict:
    data = await insertOne(
        config.DB_NAME,
        config.TABLE_TODO_LIST,
        todo
    )
    getNewData = await findOne(
        config.DB_NAME,
        config.TABLE_TODO_LIST,
        {"_id": data.inserted_id}
    )
    print('addTodo getNewData: ', getNewData)
    return todoListHelper(getNewData)


async def searchTodos():
    todos = []
    async for todo in find(config.DB_NAME, config.TABLE_TODO_LIST):
        todos.append(todoListHelper(todo))
    return todos


async def searchTodo(id: str) -> dict:
    todo = await findOne(
        config.DB_NAME,
        config.TABLE_TODO_LIST,
        {"_id": ObjectId(id)}
    )
    print('searchTodo todo:',todo)
    if todo:
        return todoListHelper(todo)


async def removeTodo(id: str):
    todo = await findOne(
        config.DB_NAME,
        config.TABLE_TODO_LIST,
        {"_id": ObjectId(id)}
    )
    print('removeTodo todo:', todo)
    if todo:
        removedTodo = await deleteOne(
            config.DB_NAME,
            config.TABLE_TODO_LIST,
            {"_id": ObjectId(id)},
        )
        if removedTodo:
            return True
        return False


async def updateTodo(id: str, data: dict):
    if len(data) < 1:
        return False

    todo = await findOne(
        config.DB_NAME,
        config.TABLE_TODO_LIST,
        {"_id": ObjectId(id)}
    )

    if todo:
        updateTodo = await updateOne(
            config.DB_NAME,
            config.TABLE_TODO_LIST,
            {"_id": ObjectId(id)},
            {"$set": data}
        )
        if updateTodo:
            return True
        return False
