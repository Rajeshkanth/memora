import time

from engines.video_engine import VideoEngine

engine = VideoEngine()

engine.initialize()

print("Video engine initiated successfully")

engine.play("media/test.mp4")

time.sleep(0.5)

while engine.is_playing():
    time.sleep(0.1)

print("Playback finished")