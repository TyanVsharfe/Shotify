from pydantic import BaseModel


class ScreenshotRequest(BaseModel):
    url: str
    is_fresh: bool = False
