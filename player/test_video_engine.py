import time
import vlc

from engines.video_engine import VideoEngine

engine = VideoEngine()

engine.initialize()

engine.play("media/test.mp4")

previous = None

while True:

    state = engine.get_state()

    if state != previous:
        print(state)
        previous = state

    if state in (vlc.State.Ended, vlc.State.Error):
        break

    time.sleep(0.05)

print("Finished")