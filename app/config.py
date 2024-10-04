# app/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    DB_CONNECTION_STRING: str = os.getenv("DB_CONNECTION_STRING")
    

settings = Settings()
