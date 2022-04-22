from prefect import task
import httpx


@task(name="Get todo", description="Get a todo from an id")
async def get_todo(task_id: int) -> dict:

    base_url = "https://jsonplaceholder.typicode.com/todos/"

    async with httpx.AsyncClient(base_url=base_url) as client:
        response = await client.get(task_id)

        return response.json()
