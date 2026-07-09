import time
import vlc

VIDEO_EXTENSIONS = [".mp4", ".mov", ".avi", ".mkv"]
IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]

class Renderer:

    def play(self, media_path):

        suffix = media_path.suffix.lower()

        if suffix in [".mp4", ".mov", ".avi", ".mkv"]:
            self.play_video(media_path)

        elif suffix in [".jpg", ".jpeg", ".png"]:
            self.show_image(media_path)

    def play_video(self, media_path):

        instance = vlc.Instance()

        player = instance.media_player_new()

        media = instance.media_new(str(media_path))

        player.set_media(media)

        player.set_fullscreen(True)

        player.play()

        time.sleep(1)

        while player.is_playing():
            time.sleep(0.5)

    def show_image(self, media_path):

        print("Image showing feature will be in future")