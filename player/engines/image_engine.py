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

        driver = sdl2.SDL_GetCurrentVideoDriver()
        print("Video Driver:", driver.decode() if driver else "None")

        self.window = sdl2.ext.Window(
            "Memora",
            size=(self.width, self.height),
            flags=sdl2.SDL_WINDOW_FULLSCREEN
        )

        self.window.show()

        self.renderer = sdl2.SDL_CreateRenderer(
            self.window.window,
            -1,
            sdl2.SDL_RENDERER_ACCELERATED
        )

        if not self.renderer:
            print("Renderer creation failed!")
            print("SDL Error:", sdl2.SDL_GetError().decode())
        else:
            print("Renderer created successfully!")

        # Set draw color to red
        sdl2.SDL_SetRenderDrawColor(
            self.renderer,
            255, 0, 0, 255
        )

        # Clear the screen using that color
        sdl2.SDL_RenderClear(self.renderer)

        # Display it
        sdl2.SDL_RenderPresent(self.renderer)

    def show(self, image_path):
        pass

    def clear(self):
        pass
        
    def shutdown(self):
        pass