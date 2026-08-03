from pathlib import Path
import shutil

from fastapi import UploadFile
from utils import is_image, is_video


class MediaService:

    MEDIA_DIR = Path("media")

    @classmethod
    def initialize(cls):
        cls.MEDIA_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def save_files(cls, files: list[UploadFile]) -> int:
        count = 0

        for file in files:
            destination = cls.MEDIA_DIR / file.filename

            with destination.open("wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            count += 1

        return count

    @staticmethod
    def list():

        media = []

        for file in sorted(MediaService.MEDIA_DIR.iterdir()):

            if not (is_image(file) or is_video(file)):
                continue

            media.append(
                {
                    "name": file.name,
                    "url": f"/media/{file.name}",
                    "thumbnail": f"/media/{file.name}",  # later videos will use generated thumbnails
                    "type": "image" if is_image(file) else "video",
                    "is_video": is_video(file),
                }
            )

        return media

    @staticmethod
    def delete(filename):

        file = MediaService.MEDIA_DIR / filename

        if file.exists():

            file.unlink()