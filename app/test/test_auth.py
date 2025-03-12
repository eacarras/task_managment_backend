# app/test/test_auth.py
import pytest
from fastapi.testclient import TestClient
from app.main import app  # Importa la app FastAPI

@pytest.mark.asyncio
async def test_register_user():
    # Simulamos una solicitud POST para registrar un nuevo usuario
    user_data = {
        "username": "nuevo_usuario",
        "password": "contraseña_secreta"
    }

    # Usamos TestClient en lugar de AsyncClient
    with TestClient(app) as client:
        response = client.post("/register", json=user_data)

    assert response.status_code == 200  # Verifica que la respuesta sea 200 OK
    assert response.json() == {"message": "Usuario registrado correctamente"}

@pytest.mark.asyncio
async def test_register_existing_user():
    user_data = {
        "username": "usuario_existente",
        "password": "contraseña_secreta"
    }

    # Registrar el usuario por primera vez
    with TestClient(app) as client:
        response = client.post("/register", json=user_data)

    # Intentamos registrar el mismo usuario de nuevo y verificar que nos dé un error
    response = client.post("/register", json=user_data)

    assert response.status_code == 400  # Debería devolver un error 400
    assert response.json() == {"detail": "El usuario ya existe"}
