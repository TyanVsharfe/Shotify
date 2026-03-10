import os
from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from starlette.responses import FileResponse

from shotify.api.MinIO.minio_db import upload_file, get_file
from shotify.api.db.database import SessionLocal, Screenshot
from shotify.api.models.Screenshot import ScreenshotRequest
from shotify.api.utils.utils import capture_screenshot


async def create_screenshot(request: ScreenshotRequest):
    db = SessionLocal()
    print(f"Request {request.url} {request.is_fresh}")
    try:
        screenshot = db.query(Screenshot).filter(Screenshot.url == request.url).first()

        if screenshot and not request.is_fresh:
            local_file_path = f"/tmp/{os.path.basename(screenshot.s3_path)}"
            file = get_file(os.path.basename(screenshot.s3_path), screenshot.s3_path)
            if file:
                return FileResponse(local_file_path, media_type="image/png")
            else:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")

        screenshot_path = capture_screenshot(request.url)
        s3_path = upload_file(screenshot_path, os.path.basename(screenshot_path))

        if not s3_path:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")

        if not screenshot:
            screenshot = Screenshot(url=request.url, s3_path=s3_path)
            db.add(screenshot)
        else:
            screenshot.s3_path = s3_path

        local_file_path = f"/tmp/{os.path.basename(s3_path)}"

        db.commit()
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Database error")
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f"Not found")
    finally:
        db.close()

    return FileResponse(local_file_path, media_type="image/png")

