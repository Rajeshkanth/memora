from pathlib import Path

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

def _is_image(path):
    return Path(path).suffix.lower() in IMAGE_EXTENSIONS

def _is_video(path):
    return Path(path).suffix.lower() in VIDEO_EXTENSIONS