from pathlib import Path
import av

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".gif",
    ".webp"
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".webm"
}

def is_image(path):
    return Path(path).suffix.lower() in IMAGE_EXTENSIONS

def is_video(path):
    return Path(path).suffix.lower() in VIDEO_EXTENSIONS

THUMBNAIL_DIR = Path("media/.thumbnails")

def generate_poster(path):
    path = Path(path)

    if not is_video(path):
        return None

    THUMBNAIL_DIR.mkdir(parents=True, exist_ok=True)

    poster_path = THUMBNAIL_DIR / f"{path.stem}.jpg"

    if poster_path.exists():
        return poster_path

    container = av.open(str(path))

    for frame in container.decode(video=0):
        frame.to_image().save(poster_path)
        break

    container.close()

    return poster_path
