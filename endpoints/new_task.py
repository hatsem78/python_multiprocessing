import time

from fastapi import APIRouter

from app_conf import Job, jobs
from core.settings import get_logger, Task
from multiprocessing import Process

from resource.producer_info import ProducerInfo

router = APIRouter()
logger = get_logger('Task Handler')


# APIs
# -----------------------------------------------------------------------------
@router.post("/")
async def task_handler(
        task: Task,
):
    """
        Add a new task to run in the background.
        - :type task: object

    """

    new_task = Job()
    try:
        param = task.value
        if param in jobs and jobs[param].result.is_alive():
            return " is raning"

        func = ProducerInfo(param, True)

        job = Process(target=func.main)
        # start the new process and new thread
        new_task.result = job
        new_task.uid = param
        jobs[new_task.uid] = new_task

        job.start()

    except Exception as ex:
        print(f"Error check_prediction: {ex}")
    return new_task.status
