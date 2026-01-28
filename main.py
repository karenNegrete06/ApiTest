#main.py fastapi dev main.py ---- ip/docs
from fastapi import FastApi,HTTPException, status
from typing import List
from uuid import UUID,uuid4
from userModel import Genero,Role,Usuario, UsuarioCreate, UsuarioUpdate


app = FastApi()


db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre="Karen",
        apellidos="Negrete",
        genero=Genero.FEMENINO,
        roles=[Role.ADMIN],
    ),

     Usuario(
        id=uuid4(),
        nombre="Angel",
        apellidos="Chamoy",
        genero=Genero.MASCULINO,
        roles=[Role.USER],
    ),
     Usuario(
        id=uuid4(),
        nombre="Tania",
        apellidos="Ibarra Salgado",
        genero=Genero.FEMENINO,
        roles=[Role.ADMIN],
    ),
     Usuario(
        id=uuid4(),
        nombre="Abril",
        apellidos="Guzman Pazos",
        genero=Genero.FEMENINO,
        roles=[Role.INVITADO],
    )
]


@app.get("/")
async def root():
    """Endpoint raíz."""
    return {"saludo": "Hola 8B IDGS hijos de Rando"}


# -------------------------
# GET
# -------------------------

@app.get("/api/v1/users", response_model=List[Usuario])
async def get_users():
    """Obtiene todos los usuarios."""
    return db


@app.get("/api/v1/users/{user_id}", response_model=Usuario)
async def get_user(user_id: UUID):
    """Obtiene un usuario por ID."""
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


# -------------------------
# POST
# -------------------------

@app.post(
    "/api/v1/users",
    response_model=Usuario,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user: UsuarioCreate):
    """Crea un nuevo usuario."""
    new_user = Usuario(id=uuid4(), **user.model_dump())
    db.append(new_user)
    return new_user


# -------------------------
# PUT
# -------------------------

@app.put("/api/v1/users/{user_id}", response_model=Usuario)
async def update_user(user_id: UUID, user_update: UsuarioUpdate):
    """Actualiza un usuario existente."""
    for index, user in enumerate(db):
        if user.id == user_id:
            updated_user = user.copy(update=user_update.model_dump())
            db[index] = updated_user
            return updated_user

    raise HTTPException(status_code=404, detail="Usuario no encontrado")


# -------------------------
# DELETE
# -------------------------

@app.delete(
    "/api/v1/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(user_id: UUID):
    """Elimina un usuario."""
    for index, user in enumerate(db):
        if user.id == user_id:
            db.pop(index)
            return None

    raise HTTPException(status_code=404, detail="Usuario no encontrado")