from core.scanner import MediaScanner
from core.playlist import Playlist
from core.renderer import Renderer
from config import Config
from constants import APP_NAME, VERSION

class MemoraPlayer:

    def __init__(self):
        self.config = Config()
        self.scanner = MediaScanner()
        self.renderer = Renderer()

    def start(self):

        print("Scanning media...")

        media = self.scanner.scan()

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

            print(f"Playing {current.name}")

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
            