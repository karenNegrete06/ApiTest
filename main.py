#main.py fastapi dev main.py ---- ip/docs
from fastapi import FastApi 
from typing import List, Optional
from uuid import UUID,uuid4
from userModel import Genero,Role,Usuario

app=FastApi()
db:List [Usuario]= [
    Usuario(
        id=uuid4(),
        nombre="Karen",
        apellidos="Negrete",
        genero=Genero.femenino,
        roles=[Role.admin],
    ),

     Usuario(
        id=uuid4(),
        nombre="Angel",
        apellidos="Chamoy",
        genero=Genero.masculino,
        roles=[Role.user],
    ),
     Usuario(
        id=uuid4(),
        nombre="Tania",
        apellidos="Ibarra Salgado",
        genero=Genero.femenino,
        roles=[Role.admin],
    ),
     Usuario(
        id=uuid4(),
        nombre="Abril",
        apellidos="Guzman Pazos",
        genero=Genero.masculino,
        roles=[Role.invitado],
    )
]

@app.get("/")
async def root():
    return {"saludo":"Hola 8B IDGS Hijos del Tio Randolfin"}

@app.get("/api/v1/users")
async def get_users():
    return db