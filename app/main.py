from fastapi import FastAPI
from pydantic import BaseModel
from app.models.user import User

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the Webapp."}

@app.post("/register/")
async def regitser(user: User):
    print("Welcome to the registration process.")
    return user

@app.get("/login")
def login():
    return {"message": "Please Log in."}

@app.get("/users")
def get_users():
    return {"message": "Welcome to the users page."}