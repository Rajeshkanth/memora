import sdl2
import sdl2.ext
from PIL import Image

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
            size=(800, 480),
            flags=sdl2.SDL_WINDOW_FULLSCREEN
        )

        self.window.show()

        # Force software renderer
        # Raspberry Pi 3A+ (Debian 13 + KMSDRM)
        # Hardware-accelerated renderer creates successfully but does not display output.
        # The software renderer renders correctly and is sufficient for an 800x480
        # digital photo frame displaying static images.
        self.renderer = sdl2.SDL_CreateRenderer(
            self.window.window,
            -1,
            sdl2.SDL_RENDERER_SOFTWARE
        )

        print("Renderer:", self.renderer)

        sdl2.SDL_SetRenderDrawColor(self.renderer, 255, 0, 0, 255)
        sdl2.SDL_RenderClear(self.renderer)
        sdl2.SDL_RenderPresent(self.renderer)

        print("Done")

    def show(self, image_path):
        image = Image.open(image_path)
        image = image.convert("RGBA")
        image = image.resize((self.width, self.height))
        image_bytes = image.tobytes()

        texture = sdl2.SDL_CreateTexture(
            self.renderer,
            sdl2.SDL_PIXELFORMAT_RGBA32,
            sdl2.SDL_TEXTUREACCESS_STATIC,
            self.width,
            self.height
        )

        sdl2.SDL_UpdateTexture(
            texture,
            None,
            image_bytes,
            self.width * 4
        )

        sdl2.SDL_RenderClear(self.renderer)

        sdl2.SDL_RenderCopy(
            self.renderer,
            texture,
            None,
            None
        )

        sdl2.SDL_RenderPresent(self.renderer)
        sdl2.SDL_DestroyTexture(texture)

    def clear(self):
        pass
        
    def shutdown(self):
        pass