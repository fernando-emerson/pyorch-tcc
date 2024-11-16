import os
import time

from celery import Celery



celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_extended = True
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "db+mysql://root:admin@localhost/dev"
)
celery.conf.broker_connection_retry_on_startup = True
celery.autodiscover_tasks(["src.automations"])



@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
