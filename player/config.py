import json
from pathlib import Path


class Config:

    def __init__(self):
        self.config_path = Path("config/config.json")

        with open(self.config_path, "r") as file:
            self.config = json.load(file)

    def _save(self):
        with open(self.config_path, "w") as file:
            json.dump(self.config, file, indent=2)

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

    def get_display_mode(self):
        return self.config.get("displayMode", "mixed")

    def set_display_mode(self, mode):
        if mode not in ("images", "videos", "mixed"):
            raise ValueError(f"Invalid display mode: {mode}")

        self.config["displayMode"] = mode
        self._save()