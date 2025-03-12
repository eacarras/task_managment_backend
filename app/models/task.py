from pydantic import BaseModel
from typing import Optional
from enum import Enum


class TaskStatus(str, Enum):
    todo = "por hacer"
    in_progress = "en progreso"
    completed = "completada"

class Task(BaseModel):
    id: Optional[str] = None  # Se generará automáticamente en MongoDB
    title: str
    description: str
    status: TaskStatus

# Definir un modelo para la solicitud PUT
class TaskUpdateRequest(BaseModel):
    new_status: TaskStatus