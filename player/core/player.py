from core.scanner import MediaScanner
from core.playlist import Playlist
from core.renderer import Renderer


class MemoraPlayer:

    def __init__(self):
        self.scanner = MediaScanner()
        self.renderer = Renderer()

    def start(self):

        print("Scanning media...")

        media = self.scanner.scan()

        playlist = Playlist(media)

        if not playlist.has_media():
            print("No media found.")
            return

        print("Playing...")

        self.renderer.play(
            playlist.current()
        )