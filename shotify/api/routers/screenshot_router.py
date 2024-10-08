import json

from fastapi import APIRouter, HTTPException

from shotify.api.models.Screenshot import ScreenshotRequest
from shotify.api.service import screenshot_service

screenshot_router = APIRouter()


@screenshot_router.post("/screenshot")
async def create_screenshot(request: ScreenshotRequest):
    try:
        result = await screenshot_service.create_screenshot(request)
        return result
    except Exception as e:
        return {"Error": str(e)}

