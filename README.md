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

The countdown timer has been integrated directly into the `Frogs/frogs.html` page as an embedded HTML/CSS/JavaScript section. Here's how it maps to the desktop specification:

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

## 5. Acceptance Criteria

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
