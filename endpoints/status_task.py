from fastapi import APIRouter

from app_conf import jobs
from core.settings import get_logger, Task

router = APIRouter()
logger = get_logger('Status Task')


# APIs
# -----------------------------------------------------------------------------
@router.get("/")
async def status_task(
        task: Task,
):
    """
        returns the status of the task.
        - :type task: object
    """
    msg = msg = f"Diff Checker Site {task.value} is finished"

    if task.value not in jobs:
        return "Is not exist"

    if jobs[task.value].result.is_alive():
        msg = f"Diff Checker Site {task.value} is progress"

    return msg
