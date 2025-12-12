Este proyecto incluye tres componentes: una API en Python (FastAPI), una API en .NET y un frontend en Angular

API en Python (FastAPI)

Requiere Python 3.10 o superior

Las dependencias se instalan usando el archivo requirements.txt

El servidor se ejecuta con uvicorn -- uvicorn app.main:app --reload --port 8000

La API queda disponible en:
http://localhost:8000

La documentación Swagger se visualiza en:
http://localhost:8000/docs

API en .NET

Requiere .NET 8

El proyecto se ejecuta con dotnet run

La API queda disponible en:
http://localhost:5072

Swagger se visualiza en:
http://localhost:5072/swagger

Frontend en Angular

Requiere Node.js y Angular CLI.

Las dependencias se manejan con npm install.

El proyecto se ejecuta con ng serve -o

El frontend queda disponible en:
http://localhost:4200

URLS usadas por Angular

Python http://localhost:8000/tasks
.NET   http://localhost:5175/api/tasks

NOTA: con el comando cd ir seleccionanado las carpetas de cada proyecto para que los comandos se ejecuten correctamente en la ruta indicada.
Cada uno en terminal diferente.
