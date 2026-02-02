from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

APP_NAME = os.getenv("APP_NAME") or "Default App Name"
APP_VERSION = os.getenv("APP_VERSION") or "0.1.0"

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

# Import routers
from backend.app.routes.user import router as user_router
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": f"{APP_NAME} backend is running 🚀"}
