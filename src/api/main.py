from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

app = FastAPI(title="AI Photography Platform")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modify this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root() -> Dict:
    """Root endpoint to verify API is running"""
    return {
        "status": "online",
        "service": "ai-photography-platform",
        "version": "0.1.0"
    }

@app.get("/health")
async def health_check() -> Dict:
    """Health check endpoint"""
    return {
        "status": "healthy",
        "components": {
            "api": "up",
            "database": "up"  # We'll implement real checks later
        }
    }