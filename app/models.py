from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    """
    Modelo ORM de usuario.

    Representa la tabla users dentro de SQLite.
    """

    __tablename__ = "users"

    # Clave primaria autoincremental.
    id = Column(Integer, primary_key=True, index=True)

    # Nombre del usuario.
    name = Column(String, nullable=False)

    # Email único.
    email = Column(String, unique=True, index=True, nullable=False)

    # Edad del usuario.
    age = Column(Integer, nullable=False)
