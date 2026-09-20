"""Application entry point for Task Manager Api."""

from fastapi import FastAPI

from src.routes.health import router as health_router


app = FastAPI(
    title="Task Manager Api",
    description="A Django REST Framework application providing endpoints for creating, retrieving, updating, and deleting tasks, with user authentication and authorization features.",
    version="1.0.0",
)

app.include_router(health_router)


@app.get("/")
def root() -> dict[str, str]:
    """Return basic service information."""

    return {
        "service": "task-manager-api",
        "version": "1.0.0",
        "status": "running",
        "message": "API is running successfully",
    }
