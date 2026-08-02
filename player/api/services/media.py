from pathlib import Path
import shutil

from fastapi import UploadFile


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