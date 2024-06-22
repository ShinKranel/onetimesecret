import uvicorn
from fastapi import FastAPI
from backend.src.secrets.router import router as secret_router

app = FastAPI(
    project_name="One Time Secret"
)

app.include_router(secret_router, tags=['secret'])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
