from fastapi import FastAPI
from pydantic import BaseModel

# Inicia el servidor con python -m uvicorn users:app --reload

#Class User

class User(BaseModel):
    name: str
    surname: str
    email: str
    age : int


users_list = [User(name="luis",surname="lcarlos",email="luiscardozoicg@gmail.com",age=32),
              User(name="carlos",surname="Carlos999",email="carlos@gmail.com",age=30),
              User(name="Katalina",surname="Kata77",email="katalina@gmail.com",age=21),
              User(name="Mauricio",surname="Maotapas",email="maotapas77@gmail.com",age=37)]


app = FastAPI()
@app.get("/users")
async def usersJson():
    return users_list