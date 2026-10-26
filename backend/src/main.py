import contextlib
from pathlib import Path

import fastapi
import fastapi.middleware.cors

from . import config, database, routes


@contextlib.asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    database.init_db()

    yield

    database.close_db()


app = fastapi.FastAPI(
    title="PostgreSQL viewer",
    version="0.0.1",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

app.include_router(routes.tables_router)


if config.settings.inside_container:
    frontend_dir = Path(__file__).resolve().parent.parent / "build" / "client"
    app.frontend("/", directory=frontend_dir)
else:
    app.add_middleware(
        fastapi.middleware.cors.CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/api/health")
async def health():
    return {"status": "healthy"}
