import sdl2
import sdl2.ext
from PIL import Image, ImageOps

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

        sdl2.SDL_ShowCursor(sdl2.SDL_DISABLE)

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

        print("Done")

    def show(self, image_path):
        image_bytes = self._prepare_image(image_path)

        self._create_texture(image_bytes)

        self._render_texture()

    def clear(self):
        sdl2.SDL_SetRenderDrawColor(
            self.renderer,
            0,
            0,
            0,
            255
        )
        sdl2.SDL_RenderClear(self.renderer)
        sdl2.SDL_RenderPresent(self.renderer)
        
    def shutdown(self):
        if self.texture:
            sdl2.SDL_DestroyTexture(self.texture)
            self.texture = None

        if self.renderer:
            sdl2.SDL_DestroyRenderer(self.renderer)

        if self.window:
            self.window.close()

        sdl2.ext.quit()

    
    def _prepare_image(self, image_path):
        image = ImageOps.exif_transpose(Image.open(image_path))
        image = image.convert("RGBA")

        image.thumbnail(
            (self.width, self.height),
            Image.Resampling.LANCZOS
        )

        canvas = Image.new(
            "RGBA",
            (self.width, self.height),
            (0, 0, 0, 255)
        )

        x = (self.width - image.width) // 2
        y = (self.height - image.height) // 2

        canvas.paste(image, (x, y))

        return canvas.tobytes()
    

    def _create_texture(self, image_bytes):

        if self.texture:
            sdl2.SDL_DestroyTexture(self.texture)
            self.texture = None

        self.texture = sdl2.SDL_CreateTexture(
            self.renderer,
            sdl2.SDL_PIXELFORMAT_RGBA32,
            sdl2.SDL_TEXTUREACCESS_STATIC,
            self.width,
            self.height
        )

        if not self.texture:
            raise RuntimeError(
                sdl2.SDL_GetError().decode()
            )

        result = sdl2.SDL_UpdateTexture(
            self.texture,
            None,
            image_bytes,
            self.width * 4
        )

        if result != 0:
            raise RuntimeError(
                sdl2.SDL_GetError().decode()
            )
        

    
    def _render_texture(self):

        sdl2.SDL_SetRenderDrawColor(
            self.renderer,
            0,
            0,
            0,
            255
        )

        sdl2.SDL_RenderClear(self.renderer)

        result = sdl2.SDL_RenderCopy(
            self.renderer,
            self.texture,
            None,
            None
        )

        if result != 0:
            raise RuntimeError(
                sdl2.SDL_GetError().decode()
            )

        sdl2.SDL_RenderPresent(self.renderer)