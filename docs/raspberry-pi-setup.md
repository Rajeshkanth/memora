# MEMORA — First Boot & Onboarding Experience

> **Vision**
>
> MEMORA should feel like a premium consumer electronics product.
> Users should never feel like they are interacting with a Raspberry Pi or a Linux computer.
>
> The experience should be simple, elegant, and emotional.

---

# First Boot

When MEMORA is powered on for the very first time, it should not start the slideshow.

Instead, the display should present a clean onboarding screen.

```
────────────────────────────

           MEMORA

      Your Living Memories

      ███████████████
      █             █
      █     QR      █
      █             █
      ███████████████

Scan to setup

or visit

memora.local

────────────────────────────
```

No desktop.

No terminal.

No settings.

No slideshow.

Only onboarding.

---

# Opening the Web App

The QR code should open

```
http://memora.local
```

or

```
http://<device-ip>
```

depending on network availability.

---

# Walkthrough

Instead of immediately opening the dashboard, guide the user through a short introduction.

---

## Screen 1

# Welcome

```
Welcome to MEMORA

Your memories deserve
a beautiful home.

[Next]
```

---

## Screen 2

# Connect MEMORA

```
Choose a Wi-Fi network
for your frame.

[Configure Wi-Fi]
```

---

## Screen 3

# Upload Memories

```
Upload your favourite
photos and videos.

[Continue]
```

---

After the walkthrough, the user is taken to the Dashboard.

---

# Dashboard

The dashboard should follow the premium design created for MEMORA.

Main sections include:

- Dashboard
- Media
- Wi-Fi
- Device
- Settings

The dashboard should feel calm, premium and minimal.

---

# Wi-Fi

The Wi-Fi page should display:

```
Connected

🟢 Home Wi-Fi

────────────────

Available Networks

Office

Guest

Phone Hotspot
```

Selecting another network opens a password dialog.

```
Connect to

Office Wi-Fi

Password

•••••••••••

[Cancel]

[Connect]
```

---

# Connecting to a New Network

When the user presses **Connect**, immediately transition to a dedicated connection screen.

```
Connecting...

MEMORA is joining

Office Wi-Fi

Please wait...

This may take
20–30 seconds.
```

The web page should not expect an HTTP response.

Changing Wi-Fi will disconnect the existing network connection.

This behaviour is expected.

---

# After Wi-Fi Changes

Once MEMORA switches networks, the browser connection will be lost.

Instead of confusing the user, display guidance beforehand.

```
Your device may disconnect.

Reconnect your phone to

Office Wi-Fi

Then open

memora.local
```

This follows the same experience used by devices such as Chromecast and Sonos.

---

# Uploading Media

Users can upload:

- Photos
- Videos

Example

```
Harry.mp4

Family.jpg

Vacation.png
```

After upload completes, the dashboard should indicate success.

```
3 Memories Added
```

---

# Starting MEMORA

Uploading media should not immediately start playback.

Instead, present one final confirmation.

```
Ready to begin?

[Start MEMORA]
```

---

When the user presses

```
Start MEMORA
```

the display should

- Fade to black
- Exit onboarding
- Launch the slideshow

---

# Normal Operation

After setup has completed, MEMORA should never display onboarding again.

The display should contain only memories.

No menus.

No controls.

No desktop.

No Linux.

Only the slideshow.

---

# Factory Reset

Factory Reset returns MEMORA to its original state.

After a reset:

- Wi-Fi is removed
- Settings are cleared
- Onboarding is shown again
- QR code is displayed again

---

# Device State Flow

```
BOOT
   │
   ▼
FIRST_SETUP
   │
   ▼
WEB_CONFIGURATION
   │
   ▼
READY
   │
   ▼
SLIDESHOW
```

Transitions:

- BOOT → FIRST_SETUP
- FIRST_SETUP → WEB_CONFIGURATION
- WEB_CONFIGURATION → READY
- READY → SLIDESHOW

On future boots:

```
BOOT
   │
   ▼
SLIDESHOW
```

unless Factory Reset is performed.

---

# Design Principle

MEMORA is not a Raspberry Pi.

MEMORA is not a file manager.

MEMORA is not a cloud storage application.

MEMORA is a digital memory frame.

Every interaction should reinforce one feeling:

> **"These are your memories, not your files."**