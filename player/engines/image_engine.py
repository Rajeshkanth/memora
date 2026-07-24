import sdl2
import sdl2.ext

class ImageEngine:

    def __init__(self):
        self.window = None
        self.renderer = None
        self.texture = None
        self.width = 800
        self.height = 480

    def initialize(self):
        sdl2.ext.init()

        self.window = sdl2.ext.Window(
            "Memora",
            size=(self.width, self.height),
            flags=sdl2.SDL_WINDOW_FULLSCREEN
        )

        self.window.show()

        self.renderer = sdl2.ext.Renderer(self.window)

        self.renderer.clear((0, 0, 0))
        self.renderer.present()

    def show(self, image_path):
        pass

    def clear(self):
        pass
        
    def shutdown(self):
        pass