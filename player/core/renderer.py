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
            self.instance = vlc.Instance(
                "--quiet",
                "--no-video-title-show",
                "--vout=drm_vout"
            )
            self.player = self.instance.media_player_new()

            time.sleep(0.3)

    def play(self, media_path):

        self.initialize()

        suffix = media_path.suffix.lower()

        if suffix in VIDEO_EXTENSIONS:
            self.play_video(media_path)

        elif suffix in IMAGE_EXTENSIONS:
            self.show_image(media_path)

    def play_video(self, media_path):

        self.player.stop()

        media = self.instance.media_new(str(media_path))

        self.player.set_media(media)

        self.player.set_fullscreen(True)

        self.player.play()

        # Wait until playback actually starts
        for _ in range(20):
            if self.player.is_playing():
                break
            time.sleep(0.1)

        while self.player.is_playing():
            time.sleep(0.2)

    def show_image(self, media_path):

        self.player.stop()

        media = self.instance.media_new(str(media_path))

        self.player.set_media(media)

        self.player.set_fullscreen(True)

        self.player.play()

        for _ in range(20):
            state = self.player.get_state()

            if state in (
                vlc.State.Playing,
                vlc.State.Paused,
            ):
                break

            time.sleep(0.1)

        time.sleep(5)

    def show_splash(self):

        self.initialize()

        splash = Path("assets") / "splash.mp4"

        self.player.stop()

        media = self.instance.media_new(str(splash))

        self.player.set_media(media)

        self.player.set_fullscreen(True)

        self.player.play()

        while self.player.is_playing():
            time.sleep(0.2)

    def show_image_forever(self, media_path):

        self.initialize()

        self.player.stop()

        media = self.instance.media_new(str(media_path))

        self.player.set_media(media)

        self.player.set_fullscreen(True)

        self.player.play()

        # Wait until the image is rendered
        for _ in range(20):
            state = self.player.get_state()

            if state in (vlc.State.Playing, vlc.State.Paused):
                break

            time.sleep(0.1)

        # Keep the image displayed forever
        while True:
            time.sleep(1)