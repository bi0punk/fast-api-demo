from pydantic import BaseModel, Field
from typing import Optional


class UserCreate(BaseModel):
    """
    Esquema para crear usuarios.

    Define qué datos debe enviar el cliente.
    """

    name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., min_length=5, max_length=100)
    age: int = Field(..., ge=1, le=120)


class UserUpdate(BaseModel):
    """
    Esquema para actualizar usuarios.

    Todos los campos son opcionales para permitir actualización parcial.
    """

    name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[str] = Field(None, min_length=5, max_length=100)
    age: Optional[int] = Field(None, ge=1, le=120)


class UserResponse(BaseModel):
    """
    Esquema de respuesta de usuarios.

    Define cómo la API devuelve los datos al cliente.
    """

    id: int
    name: str
    email: str
    age: int

    class Config:
        # Permite convertir modelos SQLAlchemy a objetos Pydantic.
        from_attributes = True
