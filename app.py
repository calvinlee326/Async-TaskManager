from fastapi import FastAPI, BackgroundTasks
from task_manager.background_tasks import long_running_task, task_worker, add_task_to_queue, task_status
import asyncio
import uuid

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the API!"}

#start background task worker to process queue
@app.on_event("startup")
async def startup_event():
    for _ in range(6):
        asyncio.create_task(task_worker())

@app.post("/run-task/")
async def run_task(task_data: dict, background_tasks: BackgroundTasks):
    """
    Endpoint to trigger a long-running task.
    :param task_data: Data needed to perform the task
    :param background_tasks: Background tasks manager for async processing
    """
    task_id = str(uuid.uuid4())  # 生成唯一的 task_id
    task_status[task_id] = "Pending"  # 更新任務狀態
    background_tasks.add_task(long_running_task, task_data, task_id)  # 傳遞 task_id
    return {"message": "Task is running in the background", "task_id": task_id}

@app.get("/status/{task_id}")
async def get_task_status(task_id: str):
    """
    Endpoint to check the status of a task.
    :param task_id: ID of the task
    """
    status = task_status.get(task_id, "Task not found")
    return {"task_id": task_id, "status": status}