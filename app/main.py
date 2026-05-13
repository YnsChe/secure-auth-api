from fastapi import FastAPI
from app.api.routes import router

'''
Creates FastAPI app
'''
app = FastAPI()
app.include_router(router)