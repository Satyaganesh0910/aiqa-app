from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from . import auth, file_upload, chat, models, database

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="AIQA API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(file_upload.router)
app.include_router(chat.router)

# Mount static files for uploads
if os.path.exists("uploads"):
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
def read_root():
    return {"message": "AIQA API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
