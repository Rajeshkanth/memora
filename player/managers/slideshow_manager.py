from pathlib import Path
import time

from engines.image_engine import ImageEngine
from engines.video_engine import VideoEngine
from utils import is_image, is_video
from managers.media_manager import MediaManager


class SlideshowManager:

    def __init__(self, media_dir):

        self.image_engine = ImageEngine()
        self.video_engine = VideoEngine()
        self.media_manager = MediaManager(media_dir)

        self.image_engine.initialize()
        self.video_engine.initialize()

        self.interval = 5
        self.running = False
        self.last_switch = 0

    def show_current(self):

        media = self.media_manager.current

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
            self.image_engine.shutdown()
            time.sleep(0.1)
            self.video_engine.play(str(media))

    def start(self, interval=5):

        self.interval = interval

        if not self.media_manager.has_media():
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

        media = self.media_manager.current

        if media is None:
            return

        if self.media_manager.refresh_required:
            print("Refreshing playlist")
            self.media_manager.refresh()

        now = time.monotonic()

        if is_image(media):

            self.video_engine.stop()

            if now - self.last_switch >= self.interval:
                self.media_manager.next()
                self.show_current()
                self.last_switch = now

        elif is_video(media):

            if self.video_engine.has_finished():
                self.media_manager.next()
                self.show_current()
                self.last_switch = now

    def shutdown(self):

        self.stop()

        self.media_manager.shutdown()
        self.image_engine.shutdown()
        self.video_engine.shutdown()