import time

from engines.image_engine import ImageEngine

engine = ImageEngine()

engine.initialize()

engine.show("media/photo1.jpg")

time.sleep(10)

# engine.show("media/photo1.jpg")

# time.sleep(5)

# engine.show("media/photo2.jpg")

# time.sleep(5)

# engine.shutdown()