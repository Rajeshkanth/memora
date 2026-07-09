from pathlib import Path
from config import Config


class MediaScanner:

    def __init__(self):
        self.config = Config()

    def scan(self):

        media_folder = Path(self.config.get_media_folder())

        if not media_folder.exists():
            return []

        media_files = []

        for file in media_folder.iterdir():

            if file.suffix.lower() in self.config.get_supported_extensions():
                media_files.append(file)

        return sorted(media_files)