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
    start_time = time.perf_counter()

    for image, pts in video.frames():

        target_time = start_time + pts

        while True:
            now = time.perf_counter()
            remaining = target_time - now

            if remaining <= 0:
                break

            time.sleep(min(remaining, 0.002))

        engine.show_pil_image(image)

finally:
    engine.shutdown()

input("Press Enter to exit...")

engine.shutdown()