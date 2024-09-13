import asyncio

async def long_running_task(task_data):
    """
    Simulate a long-running task using asyncio.sleep.
    :param task_data: Data for the task
    """
    print(f"Task started with data: {task_data}")
    # Simulate a task that takes 10 seconds to complete
    await asyncio.sleep(10)
    print(f"Task completed: {task_data}")
