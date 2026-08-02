from watchdog.events import FileSystemEventHandler


class MediaWatcher(FileSystemEventHandler):

    def __init__(self, media_manager):
        self.media_manager = media_manager

    def _request_refresh(self):

        if not self.media_manager.refresh_required:
            print("Media library changed.")
            self.media_manager.refresh_required = True

    def on_created(self, event):
        if not event.is_directory:
            print(f"Created: {event.src_path}")
            self._request_refresh()

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"Deleted: {event.src_path}")
            self._request_refresh()

    def on_moved(self, event):
        if not event.is_directory:
            print(f"Moved: {event.src_path}")
            self._request_refresh()

    def on_modified(self, event):
        if not event.is_directory:
            self._request_refresh()