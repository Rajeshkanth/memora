from library import Library
from config import Config

library = Library("config/test_library.json")

print("Default (unknown file):", library.is_enabled("a.mp4"))

library.set_enabled("a.mp4", False)
print("After disabling:", library.is_enabled("a.mp4"))

library.set_enabled("a.mp4", True)
print("After re-enabling:", library.is_enabled("a.mp4"))

library.remove("a.mp4")
print("After removing (back to default):", library.is_enabled("a.mp4"))

config = Config()
print("Current display mode:", config.get_display_mode())

config.set_display_mode("videos")
print("Display mode after set:", config.get_display_mode())

config.set_display_mode("mixed")
