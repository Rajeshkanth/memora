class Playlist:

    def has_next(self):

        return self.index < len(self.media_files) - 1

    def reset(self):

        self.index = 0

    def __init__(self, media_files):
        self.media_files = media_files
        self.index = 0

    def is_empty(self):
        return len(self.media_files) == 0

    def current(self):
        if self.is_empty():
            return None
        return self.media_files[self.index]

    def next(self):

        if self.is_empty():
            return None

        if self.has_next():
            self.index += 1

        return self.current()

    def size(self):
        return len(self.media_files)