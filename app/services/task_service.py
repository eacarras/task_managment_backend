from app.models.task import Task, TaskStatus
from app.core.config import tasks_collection
import uuid

async def create_task(task: Task):
    task_data = task.dict()
    task_data["_id"] = str(uuid.uuid4())  # Generamos un ID aleatorio
    await tasks_collection.insert_one(task_data)
    return task_data

async def get_all_tasks():
    tasks = await tasks_collection.find().to_list(1000)
    for task in tasks:
        task["id"] = task["_id"]
        del task["_id"]
    return tasks

async def update_task_status(task_id: str, new_status: TaskStatus):
    """Actualiza el estado de una tarea con ID en formato string"""
    result = tasks_collection.update_one(
        {"_id": task_id},  # 🔹 Busca por ID en string
        {"$set": {"status": new_status}}
    )

    return True

async def delete_task(task_id: str):
    result = await tasks_collection.delete_one({"_id": task_id})
    return result.deleted_count
