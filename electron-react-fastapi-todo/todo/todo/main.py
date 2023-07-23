from typing import Optional
from fastapi import FastAPI

from todo.models.models import Todo, TodoPydantic, TodoInPydantic
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


class Status(BaseModel):
    message: str


@app.get("/todos/", response_model=list[TodoPydantic])
async def get_todos():
    return await TodoPydantic.from_queryset(Todo.all())


@app.get("/todos/{todo_id}", response_model=TodoPydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_todo_by_id(todo_id: int):
    return await Todo.from_queryset_single(Todo.get(id=todo_id))


@app.put("/todos/{todo_id}", response_model=TodoPydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_todo_by_id(todo_id: int, todo: TodoPydantic):
    await Todo.filter(id=todo_id).update(**todo.dict(exclude={"id"}, exclude_unset=True))
    return await TodoPydantic.from_queryset_single(Todo.get(id=todo_id))


@app.delete("/todos/{todo_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_todo_by_id(todo_id: int):
    deleted_count = await Todo.filter(id=todo_id).delete()
    if not deleted_count:
        raise HTTPNotFoundError(status_code=404, detail=f"Todo {todo_id} not found")
    return Status(message=f"Deleted todo {todo_id}")

@app.post("/todos/", response_model=TodoPydantic)
async def create_todo(todo: TodoInPydantic):
    todo_obj = await Todo.create(**todo.dict(exclude_unset=True))
    return await TodoPydantic.from_tortoise_orm(todo_obj)


# postgres://{user}:{passwd}@{host}:5432/{db}
register_tortoise(
    app,
    db_url="postgres://unerue@localhost:5432/fastTodo",
    modules={"models": ["todo.models.models"]},
    generate_schemas=True,
    add_exception_handlers=True
)