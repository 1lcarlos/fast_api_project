from fastapi import FastAPI
from pydantic import BaseModel

# Inicia el servidor con python -m uvicorn users:app --reload

#Class User

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age : int


users_list = [User(id = 1 ,name="luis",surname="lcarlos",email="luiscardozoicg@gmail.com",age=32),
              User(id = 2 ,name="carlos",surname="Carlos999",email="carlos@gmail.com",age=30),
              User(id = 3 ,name="Katalina",surname="Kata77",email="katalina@gmail.com",age=21),
              User(id = 4 ,name="Mauricio",surname="Maotapas",email="maotapas77@gmail.com",age=37)]


app = FastAPI()
@app.get("/users")
async def usersJson():
    return users_list


@app.get("/user/{id}")
async def userJson(id: int):
    return searchUser(id)

@app.get("/userquery")
async def userJson(id: int):
    return searchUser(id)
    

def searchUser(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]

    except: 
        return {"error":"Usuario no encontrado"}