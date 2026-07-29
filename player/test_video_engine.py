import time
# import mpv

# from engines.video_engine import VideoEngine

# engine = VideoEngine()

# engine.initialize()

# print("Video engine initialized successfully")

# engine.play("media/test.mp4")

# time.sleep(0.5)

# engine.play("media/test.mp4")

# # Wait until playback actually starts
# # while True:
# #     state = engine.get_state()

# #     # if state == vlc.State.Playing:
# #     #     print("Playback started")
# #     #     break

# #     # if state in (vlc.State.Error, vlc.State.Ended):
# #     #     print(f"Playback failed: {state}")
# #     #     exit(1)

# #     time.sleep(0.1)

# # Wait until playback ends
# # while True:
# #     state = engine.get_state()

# #     if state == vlc.State.Ended:
# #         break

# #     if state == vlc.State.Error:
# #         print("Playback error")
# #         break

# #     time.sleep(0.1)

# print("Playback finished")

# tests/test_video_engine.py

from engines.video_engine import VideoEngine
from engines.image_engine import ImageEngine

video = VideoEngine()
video.open("media/test.mp4")


engine = ImageEngine()
engine.initialize()

try:
    for frame in video.frames():

        frame_start = time.perf_counter()

        engine.show_pil_image(frame)

        elapsed = time.perf_counter() - frame_start

        remaining = video.frame_duration - elapsed

        if remaining > 0:
            time.sleep(remaining)

finally:
    engine.shutdown()

input("Press Enter to exit...")

engine.shutdown()