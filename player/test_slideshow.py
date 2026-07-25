import time

from slideshow_manager import SlideshowManager

slideshow = SlideshowManager("media")

slideshow.start(interval=5)

try:
    while True:
        slideshow.update()
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nStopping slideshow...")

finally:
    slideshow.shutdown()