import prefect
from prefect import task, Flow
from prefect.storage import GitHub

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello, cloud!")


with Flow("new-flow") as flow:
    hello_task()

flow.storage = GitHub(stored_as_script=True, path="flows/new_flow.py", repo="thibauldcroonenborghs-tomtom/prefect-git", access_token_secret="GITHUB_ACCESS_TOKEN")