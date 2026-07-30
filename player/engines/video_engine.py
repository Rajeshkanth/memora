import subprocess
from pathlib import Path
import os

class VideoEngine:

    def __init__(self):
        self.process = None

    def initialize(self):
        pass

    def play(self, video_path):
        self.stop()

        print("Launching: ", video_path)

        video = str(Path(video_path).resolve())

        print(video)

        self.process = subprocess.Popen(
            [
                "mpv",
                "--fullscreen",
                "--vo=gpu",
                "--no-terminal",
                video_path,
            ],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,   # Redirects standard output away from terminal
            stderr=subprocess.DEVNULL,   # Redirects error output away from terminal
            preexec_fn=os.setpgrp,       # Detaches the process cleanly on Linux/Pi
            cwd=os.getcwd(),
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