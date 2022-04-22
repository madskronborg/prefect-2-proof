from prefect.deployments import DeploymentSpec

DeploymentSpec(
    name="get_todos_deployment",
    flow_location="/flows/get_todos.py",
    tags=["todos"],
)
