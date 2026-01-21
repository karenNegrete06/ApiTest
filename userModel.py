#
from typing import List, Optional
from uuid import UUID,uuid4
from pydantic import BaseModel

class Genero (string,Enum):
    masculino="Masculino"
    femenino="Femenino"
    otro="Otro"

class Role(string,Enum):
    admin="admin"
    user="user"
    invitado="invitado"

class Usuario(BaseModel):
    id: Optional[UUID]=uuid4()
    nombre:string
    apellidos:string
    genero:Genero
    roles:List[Role]

