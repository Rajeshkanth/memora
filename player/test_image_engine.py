import time

from engines.image_engine import ImageEngine
from player.managers.slideshow_manager import SlideshowManager

engine = ImageEngine()

engine.initialize()

slideShow = SlideshowManager(engine, "media")

slideShow.start(interval=3)

while True:
    slideShow.update()
    time.sleep(0.5)

# engine.show("media/photo1.jpg")

# time.sleep(10)

# engine.show("media/photo2.jpeg")

# time.sleep(10)

# engine.show("media/photo1.jpg")

# time.sleep(10)

# engine.show("media/photo1.jpg")

# time.sleep(5)

# engine.show("media/photo2.jpg")

# time.sleep(5)

# engine.shutdown()