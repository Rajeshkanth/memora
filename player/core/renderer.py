import time
from pathlib import Path
import vlc

VIDEO_EXTENSIONS = [".mp4", ".mov", ".avi", ".mkv"]
IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]

class Renderer:

    def __init__(self):

        self.instance = None

        self.player = None
    
    def initialize(self):

        if self.instance is None:
            self.instance = vlc.Instance()
            self.player = self.instance.media_player_new()

    def play(self, media_path):

        self.initialize()

        suffix = media_path.suffix.lower()

        if suffix in VIDEO_EXTENSIONS:
            self.play_video(media_path)

        elif suffix in IMAGE_EXTENSIONS:
            self.show_image(media_path)

    def play_video(self, media_path):

        media = self.instance.media_new(str(media_path))

        self.player.set_media(media)

        self.player.set_fullscreen(True)

        self.player.play()

        time.sleep(1)

        while self.player.is_playing():
            time.sleep(0.5)

    def show_image(self, media_path):

        media = self.instance.media_new(str(media_path))

        self.player.set_media(media)

        self.player.set_fullscreen(True)

        self.player.play()

        time.sleep(5)

    def show_splash(self):

        self.initialize()

        splash = Path("assets") / "splash.mp4"

        media = self.instance.media_new(str(splash))

        self.player.set_media(media)

        self.player.set_fullscreen(True)

        self.player.play()

        time.sleep(2)