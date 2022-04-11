from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from services.todoListService import *
from models.todoListModel import *

router = APIRouter()


@router.post("", response_description="Todo list 저장")
async def saveTodoList(todo: TodoList = Body(...)):
    data = jsonable_encoder(todo)
    serviceResult = await addTodo(data)
    return ResponseModel(serviceResult, "new todo list added successfully.")


@router.get("", response_description="전체 Todo list 가져오기")
async def getAllTodoLists():
    serviceResult = await searchTodos()
    print('getAllTodoLists serviceResult : ', serviceResult)
    return ResponseModel(serviceResult, "get all todo lists successfully.")


@router.get("/{id}", response_description="해당 Todo list 가져오기")
async def getTodoList(id):
    serviceResult = await searchTodo(id)
    return ResponseModel(serviceResult, "get one todo list successfully.")


@router.put("/{id}", response_description="Todo list 업데이트")
async def updateTodoList(id, todo: TodoList = Body(...)):
    data = jsonable_encoder(todo)
    serviceResult = await updateTodo(id, data)
    return ResponseModel(serviceResult, "new todo list added successfully.")


@router.delete("/{id}", response_description="Todo list 삭제")
async def removeTodoList(id):
    serviceResult = await removeTodo(id)
    return ResponseModel(serviceResult, "todo list removed successfully.")
