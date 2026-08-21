from pydantic import BaseModel


class MediaToggleRequest(BaseModel):
    filename: str
    enabled: bool
