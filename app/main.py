from fastapi import FastAPI
from app.api.routes import router
from app.db.database import init_db

'''
Creates FastAPI app
'''
app = FastAPI()
app.include_router(router)

init_db()