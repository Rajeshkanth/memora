from pathlib import Path


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

    def previous(self):

        if not self.media:
            return

        self.current_index = (
            self.current_index - 1
        ) % len(self.media)

        self.show_current()

    def start(self):

        self.load()

        self.show_current()