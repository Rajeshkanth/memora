from core.scanner import MediaScanner
from core.playlist import Playlist


class MemoraPlayer:

    def __init__(self):
        self.scanner = MediaScanner()

    def start(self):

        print("Scanning media folder...")

        media = self.scanner.scan()

        playlist = Playlist(media)

        print(f"Found {len(media)} media files")

        if not playlist.has_media():
            print("No media found.")
            return

        print()

        print("Current Media")

        print("----------------")

        print(playlist.current().name)