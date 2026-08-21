import time

from engines.image_engine import ImageEngine
from engines.video_engine import VideoEngine
from utils import is_image, is_video, generate_poster
from managers.media_manager import MediaManager


class SlideshowManager:

    def __init__(self, media_dir):

        self.image_engine = ImageEngine()
        self.video_engine = VideoEngine()
        self.media_manager = MediaManager(media_dir)

        self.image_engine.initialize()
        self.video_engine.initialize()

        self.interval = 5
        self.video_hold_duration = 4
        self.running = False
        self.last_switch = 0
        self.looping_single = False

    def show_current(self):

        media = self.media_manager.current

        if media is None:
            return

        if is_image(media):
            print(f"Image : {media.name}")
            self.video_engine.stop()
            if not self.image_engine.initialized:
                self.image_engine.initialize()
            self.image_engine.show(str(media))

        elif is_video(media):
            print(f"Video : {media.name}")

            poster = generate_poster(media)

            self.image_engine.clear()
            self.image_engine.shutdown()
            time.sleep(0.1)

            # If this video is the only thing in rotation, have mpv loop
            # the whole poster+video playlist internally - keeps the
            # still-then-animate rhythm on every repeat, with a single
            # continuous process (no restart, no repeated flash).
            self.looping_single = len(self.media_manager.media) == 1

            self.video_engine.play_with_poster(
                poster,
                media,
                self.video_hold_duration,
                loop_playlist=self.looping_single,
            )

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

            current = self.media_manager.current

            if current is None:
                return

            if current != media:
                self.show_current()
                self.last_switch = time.monotonic()
                return

            media = current

        now = time.monotonic()

        if is_image(media):

            self.video_engine.stop()

            if now - self.last_switch >= self.interval:
                self.media_manager.next()
                self.show_current()
                self.last_switch = now

        elif is_video(media):

            # mpv is looping the poster+video playlist internally -
            # nothing to do unless more media has since shown up.
            if self.looping_single:
                if len(self.media_manager.media) > 1:
                    self.show_current()
                    self.last_switch = now
                return

            if self.video_engine.has_finished():
                self.media_manager.next()
                self.show_current()
                self.last_switch = now

    def shutdown(self):

        self.stop()

        self.media_manager.shutdown()
        self.image_engine.shutdown()
        self.video_engine.shutdown()