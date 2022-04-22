from prefect.deployments import DeploymentSpec

DeploymentSpec(
    name="get-todos-deployment",
    flow_location="./app/flows/get_todos.py",
    tags=[
        "todos",
    ],
)
