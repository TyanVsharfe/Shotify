import os

from fastapi import HTTPException

from shotify.api.MinIO.minio_db import upload_file, get_file
from shotify.api.db.database import SessionLocal, Screenshot
from shotify.api.models.Screenshot import ScreenshotRequest
from shotify.api.utils.utils import capture_screenshot


async def create_screenshot(request: ScreenshotRequest):
    db = SessionLocal()
    try:
        screenshot = db.query(Screenshot).filter(Screenshot.url == request.url).first()

        if screenshot and not request.is_fresh:
            file = get_file(screenshot.s3_path)
            if file:
                return {"screenshot_url": screenshot.s3_path}
            else:
                raise HTTPException(status_code=404, detail="Item not found")

        screenshot_path = capture_screenshot(request.url)
        s3_path = upload_file(screenshot_path, os.path.basename(screenshot_path))

        if not s3_path:
            raise HTTPException(status_code=404, detail="Item not found")

        if not screenshot:
            screenshot = Screenshot(url=request.url, s3_path=s3_path)
            db.add(screenshot)
        else:
            screenshot.s3_path = s3_path

        db.commit()
    finally:
        db.close()

    return {"screenshot_url": s3_path}

