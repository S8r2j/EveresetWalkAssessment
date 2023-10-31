import os
from dotenv import load_dotenv

load_dotenv()

# loading the secret credentials from .env file
class Settings:
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')

settings = Settings()