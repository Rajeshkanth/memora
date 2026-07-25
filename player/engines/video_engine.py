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
        
        if not self.initialized:
            raise RuntimeError(
                "VideoEngine is not initialized."
            )

        media = self.instance.media_new(
            video_path
        )

        self.player.set_media(media)

        self.player.play()

    def stop(self):
        pass

    def is_playing(self):
        pass

    def shutdown(self):
        pass