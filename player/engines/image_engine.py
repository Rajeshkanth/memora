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
            size=(800, 480),
            flags=sdl2.SDL_WINDOW_FULLSCREEN
        )

        self.window.show()

        # # Force software renderer
        # self.renderer = sdl2.SDL_CreateRenderer(
        #     self.window.window,
        #     -1,
        #     sdl2.SDL_RENDERER_SOFTWARE
        # )

        self.renderer = sdl2.SDL_CreateRenderer(
            self.window.window,
            -1,
            sdl2.SDL_RENDERER_ACCELERATED
        )

        if not self.renderer:
            print("Falling back to software renderer...")
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
        pass

    def clear(self):
        pass
        
    def shutdown(self):
        pass