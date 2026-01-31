# main.py
from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
import os
import logging

# ----------------------------
# Load .env file explicitly
# ----------------------------
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# ----------------------------
# Logging setup
# ----------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ----------------------------
# Create FastAPI app
# ----------------------------
app = FastAPI(
    title=os.getenv("APP_NAME", "AI Autonomous Hiring Engine"),
    version=os.getenv("APP_VERSION", "0.0.1"),
    description="Enterprise-grade AI hiring platform"
)

# ----------------------------
# Include modular routes
# ----------------------------
from app.routes.root import router as root_router
app.include_router(root_router)

# ----------------------------
# Startup event
# ----------------------------
@app.on_event("startup")
def startup_event():
    logger.info(f"{os.getenv('APP_NAME')} backend is starting up... 🚀")
