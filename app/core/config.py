from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del archivo .env

# Conexión a MongoDB usando la URI configurada en Docker Compose
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "task-managment")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
tasks_collection = db["tasks"]
users_collection = db["users"]
