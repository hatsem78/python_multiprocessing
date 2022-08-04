import asyncio
from concurrent.futures.process import ProcessPoolExecutor
from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

from core.settings import get_logger

logger = get_logger('main')


class Job(BaseModel):
    uid: str = None
    status: str = "in progress"
    result: object = None


app = FastAPI()
jobs: Dict["-1", Job] = {}


async def run_in_process(fn, *args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(app.state.executor, fn, *args)  # wait and return result


def delete_all_mark(jobs):
    for job in jobs:
        jobs[job].result.stopped.set()
        print(job)


@app.on_event("startup")
async def startup_event():
    app.state.executor = ProcessPoolExecutor()


@app.on_event("shutdown")
async def on_shutdown():
    delete_all_mark(jobs)
    app.state.executor.shutdown()
