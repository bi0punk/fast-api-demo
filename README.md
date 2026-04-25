# FastAPI Learning API SQLite

Proyecto didáctico listo para enseñar FastAPI con SQLite, Swagger, SQLAlchemy y pruebas desde Linux.

## Estructura

```text
fastapi_learning_api_sqlite/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       └── users.py
├── requirements.txt
├── scripts_test.sh
└── README.md
```

## Instalación

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Swagger

```text
http://localhost:8000/docs
```

## ReDoc

```text
http://localhost:8000/redoc
```

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | / | Endpoint raíz |
| GET | /health | Healthcheck |
| GET | /users/ | Listar usuarios |
| GET | /users/{id} | Obtener usuario |
| POST | /users/ | Crear usuario |
| PUT | /users/{id} | Actualizar usuario |
| DELETE | /users/{id} | Eliminar usuario |

## Pruebas con curl

### Healthcheck

```bash
curl http://localhost:8000/health
```

### Crear usuario

```bash
curl -X POST http://localhost:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Juan Perez",
    "email": "juan@example.com",
    "age": 30
  }'
```

### Listar usuarios

```bash
curl http://localhost:8000/users/
```

### Obtener usuario

```bash
curl http://localhost:8000/users/1
```

### Actualizar usuario

```bash
curl -X PUT http://localhost:8000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"age": 31}'
```

### Eliminar usuario

```bash
curl -X DELETE http://localhost:8000/users/1
```

## Qué significa cada cosa en curl

| Parte | Significado |
|---|---|
| curl | Cliente de consola para hacer peticiones HTTP |
| -X POST | Define el método HTTP |
| -H | Agrega un header HTTP |
| Content-Type: application/json | Indica que el body es JSON |
| -d | Envía datos en el cuerpo de la petición |
| \ | Continúa el comando en otra línea |
| URL | Endpoint que recibe la petición |

## Pruebas con HTTPie

Instalar:

```bash
sudo apt update
sudo apt install -y httpie
```

Crear usuario:

```bash
http POST :8000/users/ name="Ana Torres" email="ana@example.com" age:=25
```

Listar:

```bash
http GET :8000/users/
```

Actualizar:

```bash
http PUT :8000/users/1 age:=26
```

Eliminar:

```bash
http DELETE :8000/users/1
```

## Revisar SQLite

```bash
sudo apt install -y sqlite3
sqlite3 app.db
```

Dentro de SQLite:

```sql
.tables
SELECT * FROM users;
.exit
```

## Ejecutar pruebas automáticas con curl

Con la API levantada:

```bash
chmod +x scripts_test.sh
./scripts_test.sh
```
