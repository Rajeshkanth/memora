from pathlib import Path
from watchdog.observers import Observer
from managers.media_watcher import MediaWatcher

from utils import is_image, is_video
from config import Config
from library import Library


class MediaManager:

    def __init__(self, media_dir):

        self.media_dir = Path(media_dir)
        self.config_dir = Path("config")

        self.media = []

        self.current_index = 0

        self.refresh()

        self.observer = Observer()

        handler = MediaWatcher(self)

        self.observer.schedule(
            handler,
            str(self.media_dir),
            recursive=False
        )

        self.config_dir.mkdir(parents=True, exist_ok=True)

        self.observer.schedule(
            handler,
            str(self.config_dir),
            recursive=False
        )

        self.observer.start()

        self.refresh_required = False


    def refresh(self):

        mode = Config().get_display_mode()
        library = Library()

        self.media = sorted(
            file
            for file in self.media_dir.iterdir()
            if self._is_active(file, mode, library)
        )

        if not self.media:
            self.current_index = 0
        elif self.current_index >= len(self.media):
            self.current_index = 0

        self.refresh_required = False

    @staticmethod
    def _is_active(file, mode, library):

        if mode == "images" and not is_image(file):
            return False

        if mode == "videos" and not is_video(file):
            return False

        if not (is_image(file) or is_video(file)):
            return False

        return library.is_enabled(file.name)


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

    def shutdown(self):

        self.observer.stop()
        self.observer.join()