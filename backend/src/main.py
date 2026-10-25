import contextlib
import os
from pathlib import Path

import fastapi


@contextlib.asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    yield


app = fastapi.FastAPI(
    title="PostgreSQL viewer",
    version="0.0.1",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)


@app.get("/api/health")
async def health():
    return {"status": "healthy"}


if os.getenv("INSIDE_DOCKER", "false").lower() == "true":
    frontend_dir = Path(__file__).resolve().parent.parent / "build" / "client"
    app.frontend("/", directory=frontend_dir)
