[SPEC.md](https://github.com/user-attachments/files/25770808/SPEC.md)
# Countdown Timer GUI Application Specification

## 1. Project Overview
- **Project Name:** Countdown Timer
- **Type:** Desktop GUI Application
- **Core Functionality:** A visual countdown timer with hours, minutes, and seconds input, featuring start, pause, and reset controls
- **Target Users:** Anyone needing a simple, elegant countdown timer

## 2. UI/UX Specification

### Layout Structure
- **Single Window Application** - Fixed size 400x500 pixels
- **Vertical Layout:**
  1. Title/Header area
  2. Time Display (large, prominent)
  3. Input Area (Hours, Minutes, Seconds spinners)
  4. Control Buttons (Start, Pause, Reset)
  5. Status indicator

### Visual Design
- **Color Palette:**
  - Background: #1a1a2e (dark navy)
  - Primary accent: #e94560 (coral red)
  - Secondary: #16213e (darker navy)
  - Text primary: #ffffff (white)
  - Text secondary: #a0a0a0 (gray)
  - Success/Running: #4ecca3 (teal green)
  
- **Typography:**
  - Timer display: Bold, 72px, monospace style
  - Labels: 14px, regular weight
  - Buttons: 14px, bold
  
- **Spacing:**
  - Window padding: 30px
  - Component spacing: 20px
  - Button padding: 15px horizontal, 10px vertical

### Components
1. **Timer Display** - Large digital-style numbers showing HH:MM:SS
2. **Input Spinners** - Three number inputs for Hours, Minutes, Seconds (0-23 for hours, 0-59 for minutes/seconds)
3. **Start Button** - Begins countdown, turns green when running
4. **Pause Button** - Pauses countdown (only visible when running)
5. **Reset Button** - Resets timer to initial value
6. **Status Label** - Shows "Ready", "Running", "Paused", "Complete!"

## 3. Functionality Specification

### Core Features
1. **Time Input** - Users can set countdown duration using Hours, Minutes, Seconds fields
2. **Start Countdown** - Begin the countdown from set time
3. **Pause/Resume** - Pause the countdown and resume from where it left off
4. **Reset** - Reset timer to the originally set duration
5. **Completion Alert** - Visual and optional audio indication when countdown reaches zero

### User Interactions
- Click Start → Timer begins counting down second by second
- Click Pause → Timer stops, button changes to Resume
- Click Resume → Timer continues from paused time
- Click Reset → Timer returns to input values
- When timer reaches 00:00:00 → Display shows "Complete!", flashes

### Edge Cases
- Prevent starting with all zeros
- Validate input ranges (0-23 hours, 0-59 min/sec)
- Disable input fields while timer is running
- Handle window close during countdown gracefully

## 4. Web Integration — frogs.html

The countdown timer has been integrated directly into the `/frogs.html` page as an embedded HTML/CSS/JavaScript section. Here's how it maps to the desktop specification:

### How It's Embedded
The timer is placed inside a `<section id="countdown-timer">` block in the `<body>` of `frogs.html`, positioned just below the navigation header and above the main frog content.

### HTML Structure
```html
<section id="countdown-timer" style="background-color: #1a1a2e; ...">
    <h2>COUNTDOWN TIMER</h2>
    <div id="timer-display">00:00:00</div>
    <p id="timer-status">Ready</p>
    <div> <!-- Hour, Minute, Second inputs --> </div>
    <div> <!-- Start, Pause, Reset buttons --> </div>
</section>
```

### Visual Design (matches spec)
- **Background:** `#1a1a2e` (dark navy) — same as the desktop app
- **Title accent color:** `#e94560` (coral red) — same as the desktop app
- **Timer font:** Monospace, 48px, bold white text
- **Status text:** `#a0a0a0` gray for idle, `#10b981` green for running, `#f59e0b` amber for paused, `#22d3ee` cyan for complete

### JavaScript Logic (inline `<script>` tag)
All timer logic is written in vanilla JavaScript at the bottom of `frogs.html`:

| Function | Description |
|---|---|
| `startTimer()` | Reads H/M/S inputs, validates non-zero, starts `setInterval` countdown |
| `pauseTimer()` | Stops the interval, updates button text to "RESUME" |
| `resumeTimer()` | Restarts the interval from the remaining seconds |
| `resetTimer()` | Clears the interval, re-enables inputs, restores original time |
| `countdown()` | Decrements `remainingSeconds` each second, calls `timerComplete()` at zero |
| `timerComplete()` | Clears interval, triggers a cyan flash effect on the display |

### State Variables
- `isRunning` — Whether the timer is actively counting
- `isPaused` — Whether the timer has been paused mid-count
- `remainingSeconds` — Current seconds left on the clock
- `initialSeconds` — The original starting duration (used by Reset)
- `timerInterval` — The `setInterval` handle used to start/stop the tick

### Key Behaviors
- Input fields are **disabled** while the timer is running (re-enabled on reset/complete)
- The **Pause button** is hidden by default and only shown once the timer starts
- On completion, the timer display **flashes cyan 3 times** before resetting to a static state
- Entering **all zeros** is blocked with an error message in the status label

---

## 5. Frog Monument Map Widget — frogs.html

An interactive map widget has been embedded into `frogs.html` using the **Leaflet.js** library. The map is displayed inside a custom lily-pad themed decorative section, positioned directly below the Frog Stories section.

### Map Library
- **Leaflet.js** `v1.9.4` — loaded via CDN
- **Tile layer:** OpenStreetMap (`https://{s}.tile.openstreetmap.org/`)

### CDN Links (added to `<head>`)
```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
```

### Map Configuration
| Setting | Value |
|---|---|
| Default center | `[39.5, -98.35]` (geographic center of the U.S.) |
| Default zoom | `4` |
| Max zoom | `19` |
| Map div ID | `frogMap` |
| Map height | `500px` |

### Frog Landmark Markers
Each marker uses a `🐸` emoji rendered via `L.divIcon()` (no external image dependency). Clicking a marker opens a popup with the location name and description.

| Location | Coordinates | Description |
|---|---|---|
| Frog Fountain – TCU | `[32.7093, -97.3615]` | A famous frog landmark at Texas Christian University |
| Frog Pond – Boston Common | `[42.3550, -71.0656]` | A historic pond and skating area with frog sculptures |
| Frog Rock – CT | `[41.8400, -72.3000]` | A quirky roadside attraction shaped like a giant frog |
| Frog Bay Tribal National Park – WI | `[46.7833, -90.7833]` | The first tribal national park in the U.S., named for its frog-rich wetlands |

### Custom Marker Icon
The map uses a `L.divIcon` instead of an image-based `L.icon` to guarantee the marker always renders correctly without relying on external image URLs:

```js
const frogIcon = L.divIcon({
  html: '<div style="font-size:36px;line-height:1;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.5));">🐸</div>',
  iconSize: [40, 40],
  iconAnchor: [20, 36],
  popupAnchor: [0, -38],
  className: ''
});
```

### Lily-Pad Themed Section
The map is wrapped in a `<section id="frog-map-section">` with:
- **Top & bottom border rows** of alternating 🍃 and 🪷 emoji that gently animate with a floating keyframe (`float-pad`)
- **Deep green diagonal gradient** background: `#134e1e → #1b6b2a → #27ae60 → #145a32`
- **Double-ring box-shadow** in forest green tones for a pond-like frame
- **Gradient text title** using a `#a8ff78 → #78ffd6` green-to-teal fill via `-webkit-background-clip: text`
- **Map border:** 3px solid `#2e7d32` with a green-tinted drop shadow

### CSS Classes Added
| Class / ID | Purpose |
|---|---|
| `#frog-map-section` | Outer themed section with gradient background and layered shadows |
| `.lily-pad-border` | Top/bottom emoji border strips with horizontal gradient |
| `.lily-pad` | Individual emoji with staggered floating animation |
| `.map-section-inner` | Inner padding wrapper with subtle overlay gradient |
| `.map-section-title` | Gradient-filled heading text |
| `.map-section-subtitle` | Light-green descriptive subtitle |
| `.map-section-caption` | Italic caption below the map |

### JavaScript (inline `<script>` tag)
```js
const map = L.map('frogMap').setView([39.5, -98.35], 4);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { ... }).addTo(map);

frogPlaces.forEach(place => {
  L.marker(place.coords, { icon: frogIcon })
    .addTo(map)
    .bindPopup(`<b>${place.name}</b><br>${place.desc}`);
});
```

---

## 6. Acceptance Criteria

### Visual Checkpoints
- [ ] Dark theme with coral/teal accents displays correctly
- [ ] Timer digits are large and readable
- [ ] Buttons have proper hover states
- [ ] Timer display updates every second when running

### Functional Checkpoints
- [ ] Can set hours, minutes, and seconds
- [ ] Start button begins countdown
- [ ] Pause button stops countdown
- [ ] Resume continues from paused state
- [ ] Reset returns to initial time
- [ ] Timer reaches 00:00:00 and shows completion
- [ ] Input fields disabled during countdown
