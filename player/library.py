import json
from pathlib import Path


class Library:

    def __init__(self, path="config/library.json"):
        self.path = Path(path)
        self.data = self._load()

    def _load(self):
        if not self.path.exists():
            return {"items": {}}

        with open(self.path, "r") as file:
            return json.load(file)

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.path, "w") as file:
            json.dump(self.data, file, indent=2)

    def is_enabled(self, filename):
        return self.data["items"].get(filename, {}).get("enabled", True)

    def set_enabled(self, filename, enabled):
        self.data["items"].setdefault(filename, {})["enabled"] = enabled
        self._save()

    def remove(self, filename):
        if filename in self.data["items"]:
            del self.data["items"][filename]
            self._save()
