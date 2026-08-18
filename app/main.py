"""Application entrypoint: create app, include routes, initiate the DB."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import router
from app.db.database import init_db



@asynccontextmanager
async def lifespan(_app: FastAPI):
    """Initialize application resources during startup."""
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)
