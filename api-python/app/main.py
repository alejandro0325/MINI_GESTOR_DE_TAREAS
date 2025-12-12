from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router as tasks_router

app = FastAPI(
    title="To Do APP (FastAPI)",
    description="API para gestionar tareas en memoria. Endpoints: GET/POST/PUT/DELETE /tasks",
    version="1"
)

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_router)

@app.get("/")
def root():
    return {"message": "ToDo API - FastAPI running"}
