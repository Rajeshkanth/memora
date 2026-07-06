from pathlib import Path

SUPPORTED_EXTENSIONS = [
    ".mp4",
    ".mov",
    ".avi",
    ".mkv"
]


class MediaScanner:

    def __init__(self, media_folder="media"):
        self.media_folder = Path(media_folder)

    def scan(self):
        if not self.media_folder.exists():
            return []

        media_files = []

        for file in self.media_folder.iterdir():
            if file.suffix.lower() in SUPPORTED_EXTENSIONS:
                media_files.append(file)

        return sorted(media_files)