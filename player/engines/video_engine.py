import vlc

class VideoEngine:

    def __init__(self):
        self.instance = None
        self.player = None

        self.initialized = False

    def initialize(self):
        if self.initialized:
            return

        self.instance = vlc.Instance(
            "--quiet"
        )

        self.player = self.instance.media_player_new()

        self.initialized = True

    def play(self, video_path):
        pass

    def stop(self):
        pass

    def is_playing(self):
        pass

    def shutdown(self):
        pass