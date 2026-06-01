from fastapi import FastAPI
from app.api.routes import router
from app.db.database import init_db

"""Application entrypoint: create app, include routes, initiate the DB."""
app = FastAPI()
app.include_router(router)
init_db()