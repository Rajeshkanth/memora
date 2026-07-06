class Playlist:

    def __init__(self, media_files):
        self.media_files = media_files
        self.index = 0

    def has_media(self):
        return len(self.media_files) > 0

    def current(self):
        if not self.has_media():
            return None

        return self.media_files[self.index]

    def next(self):
        if not self.has_media():
            return None

        self.index = (self.index + 1) % len(self.media_files)

        return self.current()