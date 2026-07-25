import time
import mpv

player = mpv.MPV(
    fullscreen=True,
    keep_open=False,
)

player.play("media/test.mp4")

print("Playing...")

while player.core_idle is False:
    time.sleep(0.1)

print("Finished")