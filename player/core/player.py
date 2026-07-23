from core.scanner import MediaScanner
from core.playlist import Playlist
from core.renderer import Renderer
from config import Config
from constants import APP_NAME, VERSION
import time

class MemoraPlayer:

    def __init__(self):
        self.config = Config()
        self.scanner = MediaScanner()
        self.renderer = Renderer()

    def start(self):

        media = self.scanner.scan()

        self.renderer.initialize()

        time.sleep(1)

        self.renderer.show_splash()

        print("Scanning media...")

        playlist = Playlist(media)

        if playlist.is_empty():
            print("No media found.")
            return

        print("Playing...")

        # self.renderer.play(
        #     playlist.current()
        # )

        while True:
            current = playlist.current()

            if (
                playlist.size() == 1 and
                current.suffix.lower() in [".jpg", ".jpeg", ".png"]
            ):
                print(f"Displaying {current.name}")
                self.renderer.show_image_forever(current)
                return

            self.renderer.play(current)

            if playlist.has_next():
                playlist.next()
            elif self.config.is_loop_enabled():
                playlist.reset()
            else:
                print("=" * 40)
                print(f"        {APP_NAME}")
                print(f"        All memories played")
                print("=" * 40)
                break
            