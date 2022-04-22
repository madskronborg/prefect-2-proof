# Prefect 2 Proof

## Installation

`pip install -r requirements.txt`

## Start server

`prefect orion start`

## Test deployment not working:

In root try to install with py deploymentspec:

`prefect deployment create src/deployments/get_todos_deployment.py`

or with yaml:

`prefect deployment create src/deployments/get_todos_deployment.yaml`
