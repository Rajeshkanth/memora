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
        if self.initialized:
            self.player.stop()

    def is_playing(self):
        if not self.initialized:
            return False

        return bool(self.player.is_playing())

    def shutdown(self):
        if not self.initialized:
            return

        self.player.stop()

        self.player.release()
        self.instance.release()

        self.player = None
        self.instance = None
        self.initialized = False

    def get_state(self):
        if not self.initialized:
            return None

        return self.player.get_state()