# root.py
from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/")
def root():
    return {"message": f"{os.getenv('APP_NAME')} backend is running 🚀"}
