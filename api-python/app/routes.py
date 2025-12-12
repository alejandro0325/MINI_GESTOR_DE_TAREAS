from fastapi import APIRouter, HTTPException
from typing import List
from . import crud, schemas

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("", response_model=List[schemas.Task])
def get_tasks():
    return crud.list_tasks()

@router.post("", response_model=schemas.Task, status_code=201)
def create_task(payload: schemas.TaskCreate):
    return crud.create_task(payload)

@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, payload: schemas.TaskEdit):
    updated = crud.update_task(task_id, payload)
    if updated is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    ok = crud.delete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")