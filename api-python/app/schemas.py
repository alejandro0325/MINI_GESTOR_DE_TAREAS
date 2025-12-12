from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    """
    Modelo para crear una tarea nueva.
    Aqui se pide solo lo necesario para empezar.
    """
    title: str = Field(
        ...,
        min_length=1,
        description="titulo de la tarea",
        example="comprar comida"
    )
    description: Optional[str] = Field(
        None,
        description="descripcion corta de la tarea",
        example="ir al supermercado en la tarde"
    )


class Task(BaseModel):
    """
    Modelo completo de una tarea.
    Esto es lo que devuelve la API cuando se consulta.
    """
    id: int = Field(..., description="id unico generado automaticamente", example=1)
    title: str = Field(..., description="titulo de la tarea", example="pagar servicios")
    description: Optional[str] = Field(None, description="descripcion opcional", example="pagar luz y agua")
    completed: bool = Field(..., description="indica si la tarea esta lista", example=False)
    created_at: datetime = Field(..., description="fecha de creacion", example="2025-01-01T12:00:00Z")


class TaskEdit(BaseModel):
    """
    Modelo para editar una tarea.
    Todos los campos son opcionales.
    Se usa para actualizar solo lo que se necesite.
    """
    title: Optional[str] = Field(None, description="nuevo titulo", example="titulo actualizado")
    description: Optional[str] = Field(None, description="nueva descripcion", example="detalle actualizado")
    completed: Optional[bool] = Field(None, description="nuevo estado", example=True)


class TaskUpdate(BaseModel):
    """
    Modelo rapido solo para actualizar el estado completed.
    """
    completed: bool = Field(..., description="nuevo estado de la tarea", example=True)
