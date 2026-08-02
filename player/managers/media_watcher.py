from watchdog.events import FileSystemEventHandler


class MediaWatcher(FileSystemEventHandler):

    def __init__(self, media_manager):
        self.media_manager = media_manager

    def on_created(self, event):
        if not event.is_directory:
            print(f"Created: {event.src_path}")
            self.media_manager.refresh_required = True

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"Deleted: {event.src_path}")
            self.media_manager.refresh_required = True

    def on_moved(self, event):
        if not event.is_directory:
            print(f"Moved: {event.src_path}")
            self.media_manager.refresh_required = True