from fastapi import APIRouter

from app_conf import jobs
from core.settings import get_logger, Task

router = APIRouter()
logger = get_logger('Shutdown Task')


# APIs
# -----------------------------------------------------------------------------
@router.delete("/")
async def shutdown_task(
        site: Task,
):
    """
        returns the status of the Site.
        - :type Site: object
    """
    param = site.value
    jobs[param].result.kill()

    return "Shutdown successful"
