import time

from engines.image_engine import ImageEngine
from slideshow_manager import SlideshowManager

engine = ImageEngine()

engine.initialize()

slideShow = SlideshowManager(engine, "media")

slideShow.start()

time.sleep(2)

slideShow.next()

time.sleep(2)

slideShow.previous()

time.sleep(2)

engine.shutdown()

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