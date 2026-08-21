from pathlib import Path
import shutil

from fastapi import UploadFile
from utils import is_image, is_video
from library import Library


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

        library = Library()
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
                    "enabled": library.is_enabled(file.name),
                }
            )

        return media

    @staticmethod
    def delete(filename):

        file = MediaService.MEDIA_DIR / filename

        if file.exists():

            file.unlink()

        Library().remove(filename)

    @staticmethod
    def toggle(filename, enabled):

        Library().set_enabled(filename, enabled)