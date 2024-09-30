from fastapi import APIRouter

from shotify.api.models.Screenshot import ScreenshotRequest
from shotify.api.service import screenshot_service

screenshot_router = APIRouter()


@screenshot_router.post("/screenshot")
async def create_screenshot(request: ScreenshotRequest):
    await screenshot_service.create_screenshot(request)

