from fastapi import APIRouter, HTTPException, Depends
from app.services.auth_service import get_current_user
from app.services.task_service import create_task, get_all_tasks, update_task_status, delete_task
from app.models.task import Task, TaskUpdateRequest

router = APIRouter()

@router.post("/tasks", dependencies=[Depends(get_current_user)])
async def add_task(task: Task):
    new_task = await create_task(task)
    return new_task

@router.get("/tasks", dependencies=[Depends(get_current_user)])
async def list_tasks():
    return await get_all_tasks()

@router.put("/tasks/{task_id}", dependencies=[Depends(get_current_user)])
async def change_task_status(task_id: str, request: TaskUpdateRequest):
    updated = await update_task_status(task_id, request.new_status)
    if not updated:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Estado actualizado"}

@router.delete("/tasks/{task_id}", dependencies=[Depends(get_current_user)])
async def remove_task(task_id: str):
    deleted = await delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Tarea eliminada"}
