import sdl2
import sdl2.ext
from PIL import Image, ImageOps
from collections import OrderedDict
import time

class ImageEngine:

    def __init__(self):
        self.window = None
        self.renderer = None
        self.width = 800
        self.height = 480
        self.current_texture = None
        self.texture_cache = OrderedDict()
        self.cache_size = 5
        self.initialized = False

    def initialize(self):
        sdl2.ext.init()

        driver = sdl2.SDL_GetCurrentVideoDriver()
        print(driver.decode())

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

        self.initialized = True

        if not self.renderer:
            raise RuntimeError(sdl2.SDL_GetError().decode())
        print("Done")

    def show(self, image_path):
        """
        Loads and displays an image in fullscreen.
        """

        if not self.initialized:
            self.initialize()
        
        texture = self.texture_cache.get(image_path)

        if texture:
            print(f"Cache Hit : {image_path}")
            self.texture_cache.move_to_end(image_path)
        else:
            print(f"Cache Miss : {image_path}")
            image_bytes = self._prepare_image(image_path)
            texture = self._create_texture(image_bytes)

            self.texture_cache[image_path] = texture

            if len(self.texture_cache) > self.cache_size:
                old_path, old_texture = self.texture_cache.popitem(last=False)
                print(f"Evicted : {old_path}")
                sdl2.SDL_DestroyTexture(old_texture)

        if self.current_texture is None:
            # First image
            self.current_texture = texture

            self._clear()
            self._render_texture(texture)
            self._present()

        else:
            # Every image after the first
            self.fade_to(texture)

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
        for texture in self.texture_cache.values():
            sdl2.SDL_DestroyTexture(texture)

        self.texture_cache.clear()
        self.current_texture = None

        if self.renderer:
            sdl2.SDL_DestroyRenderer(self.renderer)

        if self.window:
            self.window.close()

        sdl2.ext.quit()

        self.initialized = False

    
    def _prepare_image(self, image_path):
        """
        Loads an image, applies EXIF orientation,
        preserves aspect ratio, and returns RGBA bytes.
        """
        try:
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
        
        except Exception as e:
            raise RuntimeError(
                f"Failed to load '{image_path}': {e}"
            )
    

    def _create_texture(self, image_bytes):

        texture = sdl2.SDL_CreateTexture(
            self.renderer,
            sdl2.SDL_PIXELFORMAT_RGBA32,
            sdl2.SDL_TEXTUREACCESS_STATIC,
            self.width,
            self.height
        )

        if not texture:
            raise RuntimeError(sdl2.SDL_GetError().decode())
        
        sdl2.SDL_SetTextureBlendMode(
            texture,
            sdl2.SDL_BLENDMODE_BLEND
        )

        result = sdl2.SDL_UpdateTexture(
            texture,
            None,
            image_bytes,
            self.width * 4
        )

        if result != 0:
            sdl2.SDL_DestroyTexture(texture)
            raise RuntimeError(sdl2.SDL_GetError().decode())

        return texture
        

    
    def _render_texture(self, texture, alpha=255):

        # self.clear()

        sdl2.SDL_SetTextureAlphaMod(
            texture,
            alpha
        )

        result = sdl2.SDL_RenderCopy(
            self.renderer,
            texture,
            None,
            None
        )

        if result != 0:
            raise RuntimeError(
                sdl2.SDL_GetError().decode()
            )

        # sdl2.SDL_RenderPresent(self.renderer)

    def _present(self):

        sdl2.SDL_RenderPresent(self.renderer)

    def _clear(self):

        sdl2.SDL_SetRenderDrawColor(
            self.renderer,
            0,
            0,
            0,
            255
        )

        sdl2.SDL_RenderClear(self.renderer)

    def fade_to(self, next_texture, duration=0.4):

        fps = 60
        steps = int(duration * fps)
        delay = 1 / fps

        for i in range(steps + 1):

            alpha = int((i / steps) * 255)

            self._clear()

            # Draw current image fading out
            self._render_texture(
                self.current_texture,
                255 - alpha
            )

            # Draw next image fading in
            self._render_texture(
                next_texture,
                alpha
            )

            self._present()

            time.sleep(delay)

        self.current_texture = next_texture