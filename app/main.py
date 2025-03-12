from fastapi import FastAPI
from app.routes.task_routes import router as task_router
from app.routes.auth_routes import router as auth_router

app = FastAPI()

app.include_router(task_router)
app.include_router(auth_router)

@app.get("/health")
def home():
    return {"message": "Task Management API is health and running 🚀"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
