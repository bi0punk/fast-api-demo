from fastapi import FastAPI

from app.database import Base, engine
from app.routers import users

# Crea las tablas automáticamente si no existen.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Learning API SQLite",
    description="API didáctica con FastAPI, Swagger, CRUD, validaciones, SQLAlchemy y SQLite.",
    version="1.0.0"
)


@app.get("/", tags=["Root"])
def root():
    """
    Endpoint raíz.

    Sirve para verificar que la API está funcionando.
    """
    return {
        "message": "FastAPI + SQLite funcionando correctamente",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", tags=["Health"])
def health_check():
    """
    Endpoint de salud.

    Útil para monitoreo, pruebas automáticas y balanceadores.
    """
    return {
        "status": "ok",
        "database": "sqlite",
        "service": "fastapi_learning_api_sqlite"
    }


# Registra las rutas de usuarios.
app.include_router(users.router)
