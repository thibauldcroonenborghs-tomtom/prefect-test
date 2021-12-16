import prefect
from prefect import task, Flow
from prefect.storage import Local

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello, Cloud!")


with Flow("hello-flow", storage=Local(stored_as_script=True, path="/Users/croonenb/git/other/prefect-test")) as flow:
    hello_task()

flow.register(project_name="test-project")
