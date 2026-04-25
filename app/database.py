from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite crea automáticamente el archivo app.db en la raíz del proyecto.
DATABASE_URL = "sqlite:///./app.db"

# check_same_thread=False permite usar SQLite con FastAPI.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Factory para crear sesiones de base de datos.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para los modelos ORM.
Base = declarative_base()


def get_db():
    """
    Crea una sesión de base de datos por request.

    FastAPI usa esta función como dependencia.
    Al finalizar el request, la sesión se cierra automáticamente.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
