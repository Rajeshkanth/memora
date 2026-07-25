import subprocess


class VideoEngine:

    def __init__(self):
        self.process = None

    def initialize(self):
        pass

    def play(self, video_path):
        self.stop()

        self.process = subprocess.Popen(
            [
                "mpv",
                "--fullscreen",
                "--no-terminal",
                "--really-quiet",
                video_path,
            ]
        )

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()

        self.process = None

    def has_finished(self):
        if self.process is None:
            return True

        return self.process.poll() is not None

    def shutdown(self):
        self.stop()