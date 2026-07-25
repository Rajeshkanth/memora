from pathlib import Path
import time


class SlideshowManager:

    def __init__(self, image_engine, media_dir):
        self.engine = image_engine
        self.media_dir = Path(media_dir)

        self.media = []
        self.current_index = 0

        self.supported_formats = {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
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

        image = self.current()

        if image:
            self.engine.show(str(image))

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

    def start(self, interval=5):

        self.interval = interval

        self.load()

        self.show_current()

        self.last_switch = time.monotonic()

        self.running = True

    
    def stop(self):

        self.running = False

    def update(self):

        if not self.running:
            return

        now = time.monotonic()

        if now - self.last_switch >= self.interval:

            self.next()

            self.last_switch = now