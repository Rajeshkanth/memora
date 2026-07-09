import json
from pathlib import Path


class Config:

    def __init__(self):
        config_path = Path("config/config.json")

        with open(config_path, "r") as file:
            self.config = json.load(file)

    def get_media_folder(self):
        return self.config["mediaFolder"]

    def get_supported_extensions(self):
        return (
            self.config["supportedVideoExtensions"]
            + self.config["supportedImageExtensions"]
        )

    def is_loop_enabled(self):
        return self.config["loop"]

    def is_shuffle_enabled(self):
        return self.config["shuffle"]