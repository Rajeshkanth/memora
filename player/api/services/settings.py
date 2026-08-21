from config import Config


class SettingsService:

    @staticmethod
    def get_display_mode():
        return Config().get_display_mode()

    @staticmethod
    def set_display_mode(mode):
        Config().set_display_mode(mode)
