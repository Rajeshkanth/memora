# import subprocess
# from pathlib import Path
# import os

# class VideoEngine:

#     def __init__(self):
#         self.process = None

#     def initialize(self):
#         pass

#     def play(self, video_path):
#         self.stop()

#         print("Launching: ", video_path)

#         video = str(Path(video_path).resolve())

#         print(video)

#         self.process = subprocess.Popen(
#             [
#                 "mpv",
#                 "--fullscreen",
#                 "--vo=sdl",
#                 video_path,
#             ],
#             stdin=subprocess.DEVNULL,
#             stdout=None,
#             stderr=None,
#             start_new_session=True,
#             cwd=os.getcwd(),
#         )

#     def stop(self):
#         if self.process and self.process.poll() is None:
#             self.process.terminate()
#             self.process.wait()

#         self.process = None

#     def has_finished(self):
#         if self.process is None:
#             return True

#         return self.process.poll() is not None

#     def shutdown(self):
#         self.stop()


import av


class VideoEngine:

    def __init__(self):
        self.container = None
        self.stream = None

    def open(self, video_path):

        self.container = av.open(video_path)
        self.stream = self.container.streams.video[0]

        print("Video opened successfully.")

        print(f"Resolution : {self.stream.width} x {self.stream.height}")

        print(f"FPS : {float(self.stream.average_rate):.2f}")

        print(f"Frames : {self.stream.frames}")

        print(f"Duration : {float(self.stream.duration * self.stream.time_base):.2f} sec")