# Memora Roadmap

## Vision

Memora is a digital living memory frame that allows users to manage photos and videos wirelessly. The goal is to create a seamless experience where memories are displayed naturally, with videos behaving like "living photos" rather than traditional media playback.

---

## Current Architecture

```
                SlideshowManager
                       │
        ┌──────────────┴──────────────┐
        │                             │
   ImageEngine                  VideoEngine
      (SDL2)                       (MPV)
        │                             │
        └────────── MediaManager ─────┘
```

### Design Principles

- Images are rendered only by `ImageEngine`.
- Videos are played only by `VideoEngine`.
- `SlideshowManager` controls media flow and engine switching.
- Avoid merging image and video rendering into a single engine.

---

# Roadmap

## Phase 1 - Media Engine

### Completed

- [x] Image slideshow
- [x] Image transitions
- [x] Image caching
- [x] Video playback using MPV
- [x] Mixed image/video slideshow

### Pending

- [ ] Reduce terminal flash during Image → Video transition (Deferred)

---

## Phase 2 - Connectivity

### Wi-Fi Configuration

- [ ] First boot setup
- [ ] Wi-Fi provisioning
- [ ] Store Wi-Fi credentials
- [ ] Auto reconnect on boot

### Web Application

- [ ] REST API
- [ ] Responsive web interface
- [ ] Gallery view
- [ ] Settings page

### Media Management

- [ ] Upload images
- [ ] Upload videos
- [ ] Delete media
- [ ] Automatic slideshow refresh

---

## Phase 3 - Living Memories

### Video Experience

Instead of immediately playing a video:

```
Thumbnail
    ↓
Display as still image
    ↓
Wait for configured duration
    ↓
Play video
```

This creates a "living photo" effect inspired by magical photo frames.

### Features

- [ ] Generate thumbnail from first video frame
- [ ] Configurable thumbnail delay
- [ ] Smooth transition to video
- [ ] Optional freeze on last frame

---

## Phase 4 - Polish

- [ ] Hide terminal flash during engine switch
- [ ] Improve transition animations
- [ ] Performance optimization
- [ ] Startup optimization
- [ ] Better error handling

---

## Future Enhancements

- QR-based upload
- Albums
- Clock & weather widgets
- Cloud synchronization
- Mobile application

---

## Development Guidelines

- Do not redesign the media architecture unless absolutely necessary.
- Complete the current phase before moving to the next.
- Defer non-blocking optimizations until the Polish phase.
- Prioritize user-facing features over internal optimizations.

---

## MVP Goal

A user should be able to:

1. Power on Memora.
2. Connect it to Wi-Fi.
3. Open the web interface.
4. Upload photos and videos.
5. See uploaded media appear automatically in the slideshow.
6. Experience videos as "living memories" through delayed playback.