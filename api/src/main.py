from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
import uvicorn
from src.database import db
from src.automations.views import router as automations_router
from src.workers.views import router as workers_router
from src.tasks.views import router as tasks_router
from src.dashboard.views import router as dashboard_router
from src.logs.views import router as logs_router

def build_app():
    app = FastAPI(**settings.set_backend_app_attributes)

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = build_app()
app.include_router(automations_router)
app.include_router(workers_router)
app.include_router(tasks_router)
app.include_router(dashboard_router)
app.include_router(logs_router)


@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "Welcome to my post application",
        "instruction": "type /docs in the url to access the api documentation",
    }


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        workers=settings.SERVER_WORKERS,
        ws_ping_timeout=300,
    )
