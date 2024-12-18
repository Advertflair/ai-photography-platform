import os
from typing import Dict, Any
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# API Settings
API_V1_STR = "/api/v1"
PROJECT_NAME = "AI Photography Platform"

# Security settings
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")  # Change in production
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 8 days

# AWS Settings
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-west-2")
S3_BUCKET = os.getenv("S3_BUCKET")

# OpenAI Settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Database settings
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Redis settings
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")