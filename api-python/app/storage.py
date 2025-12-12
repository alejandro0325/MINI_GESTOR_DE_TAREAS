# almacenamiento en memoria
from datetime import datetime
from typing import List, Dict, Optional

_tasks: List[Dict] = []
_next_id = 1

def _now_iso():
    return datetime.utcnow()

def list_all() -> List[Dict]:
    return list(_tasks)

def create_task(title: str, description: Optional[str] = None) -> Dict:
    global _next_id
    task = {
        "id": _next_id,
        "title": title,
        "description": description,
        "completed": False,
        "created_at": _now_iso()
    }
    _tasks.append(task)
    _next_id += 1
    return task

def get_task(task_id: int) -> Optional[Dict]:
    for t in _tasks:
        if t["id"] == task_id:
            return t
    return None

def update_task(task_id: int, title=None, description=None, completed=None) -> Optional[Dict]:
    task = get_task(task_id)
    if not task:
        return None

    if title is not None:
        task["title"] = title

    if description is not None:
        task["description"] = description

    if completed is not None:
        task["completed"] = bool(completed)

    return task

def delete_task(task_id: int) -> bool:
    task = get_task(task_id)
    if not task:
        return False
    _tasks.remove(task)
    return True
