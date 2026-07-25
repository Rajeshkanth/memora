import time
from engines.video_engine import VideoEngine

engine = VideoEngine()

engine.initialize()

engine.play("media/test.mp4")

print("Video started")

while not engine.has_finished():
    time.sleep(0.2)

print("Video finished")

engine.shutdown()