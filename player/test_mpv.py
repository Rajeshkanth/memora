import time
import mpv

finished = False


def on_end(event):
    global finished
    print("Playback finished")
    finished = True


player = mpv.MPV(
    fullscreen=True,
    keep_open=False,
)

player.register_event_callback(on_end)

print("Starting video...")

player.play("media/test.mp4")

# Give MPV time to start playback
time.sleep(1)

while not finished:
    time.sleep(0.1)

print("Done")