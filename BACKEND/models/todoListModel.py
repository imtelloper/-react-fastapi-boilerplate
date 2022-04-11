from pydantic import BaseModel, Field

__all__ = ["TodoList", "ResponseModel"]


class TodoList(BaseModel):
    content: str
    done: bool
    date: str


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
