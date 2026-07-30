from pathlib import Path
import time

from engines.image_engine import ImageEngine
from engines.video_engine import VideoEngine
from utils import is_image, is_video


class SlideshowManager:

    def __init__(self, media_dir):

        self.image_engine = ImageEngine()
        self.video_engine = VideoEngine()

        self.image_engine.initialize()
        self.video_engine.initialize()

        self.media_dir = Path(media_dir)

        self.media = []
        self.current_index = 0

        self.supported_formats = {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
            ".bmp",
            ".gif",
            ".mp4",
            ".mov",
            ".avi",
            ".mkv",
            ".webm",
        }

        self.interval = 5
        self.running = False
        self.last_switch = 0

    def load(self):

        self.media = sorted(
            file
            for file in self.media_dir.iterdir()
            if file.suffix.lower() in self.supported_formats
        )

        self.current_index = 0

    def current(self):

        if not self.media:
            return None

        return self.media[self.current_index]

    def show_current(self):

        media = self.current()

        if media is None:
            return

        if is_image(media):
            print(f"Image : {media.name}")
            if not self.image_engine.initialized:
                self.image_engine.initialize()
            # self.video_engine.stop()
            self.image_engine.show(str(media))

        elif is_video(media):
            print(f"Video : {media.name}")
            self.image_engine.clear()
            self.image_engine.clear_black()
            self.image_engine.shutdown()
            time.sleep(0.1)
            self.video_engine.play(str(media))

    def next(self):

        if not self.media:
            return

        self.current_index = (
            self.current_index + 1
        ) % len(self.media)

        self.show_current()

        self.last_switch = time.monotonic()

    def previous(self):

        if not self.media:
            return

        self.current_index = (
            self.current_index - 1
        ) % len(self.media)

        self.show_current()

        self.last_switch = time.monotonic()

    def start(self, interval=5):

        self.interval = interval

        self.load()

        if not self.media:
            return

        self.running = True

        self.show_current()

        self.last_switch = time.monotonic()

    def stop(self):

        self.running = False

        self.video_engine.stop()

    def update(self):

        if not self.running:
            return

        media = self.current()

        if media is None:
            return

        now = time.monotonic()

        if is_image(media):

            if now - self.last_switch >= self.interval:
                self.next()

        elif is_video(media):

            if self.video_engine.has_finished():
                self.next()

    def shutdown(self):

        self.stop()

        self.image_engine.shutdown()
        self.video_engine.shutdown()