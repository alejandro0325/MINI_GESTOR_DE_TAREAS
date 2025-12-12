from . import storage
from .schemas import TaskCreate, TaskEdit
from typing import List, Optional, Dict

def list_tasks() -> List[Dict]:
    return storage.list_all()

def create_task(payload: TaskCreate) -> Dict:
    return storage.create_task(payload.title, payload.description)

def update_task(task_id: int, payload: TaskEdit) -> Optional[Dict]:
    return storage.update_task(
        task_id,
        title=payload.title,
        description=payload.description,
        completed=payload.completed
    )

def delete_task(task_id: int) -> bool:
    return storage.delete_task(task_id)

def get_task(task_id: int) -> Optional[Dict]:
    return storage.get_task(task_id)
