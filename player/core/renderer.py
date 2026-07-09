import time
import vlc


class Renderer:

    def play(self, media_path):

        instance = vlc.Instance()

        player = instance.media_player_new()

        media = instance.media_new(str(media_path))

        player.set_media(media)

        player.set_fullscreen(True)

        player.play()

        time.sleep(1)

        while player.is_playing():
            time.sleep(0.5)