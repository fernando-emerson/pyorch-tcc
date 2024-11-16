import subprocess
from src.task_execution.task_events import CeleryTaskExecutionBackend
from src.worker import celery
import os


@celery.task(
    name="automations.projects.run", base=CeleryTaskExecutionBackend, bind=True
)
def run_task(self, project_path: str):
    result = subprocess.run(
        ["python", "main.py"],
        check=True,
        cwd=project_path,
        capture_output=True,
        text=True,
    )

    taskid = self.request.id
    automation_id = project_path.split("/")[-1]
    logs_path = f"logs/{automation_id}"

    if not os.path.exists(logs_path):
        os.mkdir(logs_path)

    with open(os.path.join(logs_path, f"{taskid}.log"), "w") as file:
        file.write(result.stdout)

    if result.returncode != 0:
        raise Exception(result.stderr)

    return result.stderr
