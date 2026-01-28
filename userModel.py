
"""
Modelos de dominio relacionados con usuarios del sistema.
"""

from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Genero(str, Enum):
    """Enum que representa el género del usuario."""

    MASCULINO = "masculino"
    FEMENINO = "femenino"
    OTRO = "otro"


class Role(str, Enum):
    """Enum que representa los roles del usuario."""

    ADMIN = "admin"
    USER = "user"
    INVITADO = "invitado"


class UsuarioBase(BaseModel):
    """Campos base compartidos para usuarios."""

    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]


class UsuarioCreate(UsuarioBase):
    """Modelo para crear usuarios (POST)."""


class UsuarioUpdate(UsuarioBase):
    """Modelo para actualizar usuarios (PUT)."""


class Usuario(UsuarioBase):
    """Modelo completo de usuario."""

    id: UUID = Field(default_factory=uuid4)
