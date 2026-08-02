from pathlib import Path

from utils import is_image, is_video


class MediaManager:

    def __init__(self, media_dir):

        self.media_dir = Path(media_dir)

        self.media = []

        self.current_index = 0

        self.refresh()


    def refresh(self):

        self.media = sorted(
            file
            for file in self.media_dir.iterdir()
            if is_image(file) or is_video(file)
        )

        if not self.media:
            self.current_index = 0
        elif self.current_index >= len(self.media):
            self.current_index = 0


    @property
    def current(self):

        if not self.media:
            return None

        return self.media[self.current_index]


    def next(self):

        if not self.media:
            return None

        self.current_index = (
            self.current_index + 1
        ) % len(self.media)

        return self.current

    def has_media(self):
        return len(self.media) > 0