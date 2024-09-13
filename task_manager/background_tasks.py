import asyncio

task_queue = asyncio.Queue()
MAX_CONCURRENT_TASKS = 6

task_status = {}
    
async def long_running_task(task_data, task_id):
    """
    Simulate a long-running task using asyncio.sleep.
    :param task_data: Data for the task
    :param task_id: ID of the task
    """
    task_status[task_id] = "In progress"
    print(f"Task started with data: {task_data}")
    await asyncio.sleep(10)
    print(f"Task completed: {task_data}")
    print(f"Task {task_id} completed")
    task_status[task_id] = "Completed"

async def task_worker():
    """
    Worker function to process tasks in the background.
    """
    while True:
        task_data, task_id = await task_queue.get()
        try:
            await long_running_task(task_data, task_id)
        finally:
            task_queue.task_done()

async def add_task_to_queue(task_data, task_id):
    """
    Add a task to the queue.
    start processing the task in the background.(if not already running)
    """
    task_status[task_id] = "Pending"
    await task_queue.put((task_data, task_id))

