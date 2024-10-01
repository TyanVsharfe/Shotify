import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")

    MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT')
    MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
    MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')

    SELENIUM_HOST = os.getenv('SELENIUM_HOST')

    BACKEND_CORS_ORIGINS: list[str] = ["http://127.0.0.1:8000",
                                       "http://localhost:8000"]


settings = Settings()
