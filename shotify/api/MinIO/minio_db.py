from fastapi import HTTPException
from minio import Minio
from minio.error import S3Error

from shotify.api.config import settings

minio_client = Minio(
    settings.MINIO_ENDPOINT.replace("http://", ""),
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False
)

BUCKET_NAME = "screenshots"


def upload_file(file_path, object_name):
    if not minio_client.bucket_exists(BUCKET_NAME):
        minio_client.make_bucket(BUCKET_NAME)
    minio_client.fput_object(BUCKET_NAME, object_name, file_path)
    return f"{BUCKET_NAME}/{object_name}"


def get_file(object_name, path):
    try:
        return minio_client.fget_object(bucket_name=BUCKET_NAME, object_name=object_name, file_path=path)
    except S3Error as err:
        raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
