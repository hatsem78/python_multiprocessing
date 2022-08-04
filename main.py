import uvicorn

from app_conf import app
from endpoints import new_task, status_task, shutdown_task

app.include_router(
    new_task.router,
    prefix="/new_task",
    tags=["New Task"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    shutdown_task.router,
    prefix="/shutdown_task",
    tags=["Shutdown Task"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    status_task.router,
    prefix="/status_task",
    tags=["Status Task"],
    responses={404: {"description": "Not found"}},
)




# Main (Fastapi debug)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8086, timeout_keep_alive=0)
