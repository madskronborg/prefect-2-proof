from app import tasks
from prefect import flow


@flow(name="Get todos flow", description="Get a list of todos from a list of todo ids")
async def get_todos(todo_ids: list[int]) -> list[dict]:

    todos: list[int] = []

    async for todo_id in todo_ids:

        todo = await tasks.get_todo(todo_id)

        todos.append(todo)

    return todo
