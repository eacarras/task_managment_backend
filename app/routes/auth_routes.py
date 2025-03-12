from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.services.auth_service import decode_access_token, create_access_token, verify_password, get_password_hash
from app.core.config import users_collection
from app.models.user import UserCreate

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/register")
async def register_user(user: UserCreate):
    """Registra un nuevo usuario"""
    existing_user = await users_collection.find_one({"username": user.username})
    print(existing_user)
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    hashed_password = get_password_hash(user.password)
    users_collection.insert_one({"username": user.username, "password": hashed_password})
    return { "message": "Usuario registrado correctamente" }

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Autentica un usuario y devuelve un token JWT"""
    user = await users_collection.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Obtiene el usuario actual a partir del token"""
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    
    username = payload.get("sub")
    user = await users_collection.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    
    return user
