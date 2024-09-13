from fastapi import FastAPI, BackgroundTasks
from task_manager.background_tasks import long_running_task

app = FastAPI()

@app.post("/run-task/")
async def run_task(task_data: dict, background_tasks: BackgroundTasks):
    """
    Endpoint to trigger a long-running task.
    :param task_data: Data needed to perform the task
    :param background_tasks: Background tasks manager for async processing
    """
    background_tasks.add_task(long_running_task, task_data)
    return {"message": "Task is running in the background"}
