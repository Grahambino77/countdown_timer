"""
Countdown Timer GUI Application
A simple and reliable countdown timer.
"""

import tkinter as tk
import threading
import time


class CountdownTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("400x450")
        self.root.configure(bg='#1a1a2e')
        
        # Timer state
        self.is_running = False
        self.is_paused = False
        self.remaining_seconds = 0
        self.initial_seconds = 0
        self.timer_thread = None
        self.stop_event = threading.Event()
        
        # Create UI
        self.create_ui()
        
    def create_ui(self):
        # Title
        title = tk.Label(self.root, text="COUNTDOWN TIMER", font=("Arial", 20, "bold"),
                        bg='#1a1a2e', fg='#e94560')
        title.pack(pady=20)
        
        # Timer display
        self.timer_label = tk.Label(self.root, text="00:00:00", font=("Courier", 48, "bold"),
                                   bg='#1a1a2e', fg='white')
        self.timer_label.pack(pady=20)
        
        # Status
        self.status_label = tk.Label(self.root, text="Ready", font=("Arial", 12),
                                    bg='#1a1a2e', fg='#a0a0a0')
        self.status_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#1a1a2e')
        input_frame.pack(pady=20)
        
        # Hours spinbox with up/down arrows
        tk.Label(input_frame, text="Hours:", bg='#1a1a2e', fg='white').grid(row=0, column=0, padx=5)
        self.hours_entry = tk.Spinbox(input_frame, from_=0, to=23, width=5, font=("Arial", 14), justify='center')
        self.hours_entry.grid(row=0, column=1, padx=5)
        
        # Minutes spinbox with up/down arrows
        tk.Label(input_frame, text="Minutes:", bg='#1a1a2e', fg='white').grid(row=0, column=2, padx=5)
        self.minutes_entry = tk.Spinbox(input_frame, from_=0, to=59, width=5, font=("Arial", 14), justify='center')
        self.minutes_entry.grid(row=0, column=3, padx=5)
        
        # Seconds spinbox with up/down arrows
        tk.Label(input_frame, text="Seconds:", bg='#1a1a2e', fg='white').grid(row=0, column=4, padx=5)
        self.seconds_entry = tk.Spinbox(input_frame, from_=0, to=59, width=5, font=("Arial", 14), justify='center')
        self.seconds_entry.grid(row=0, column=5, padx=5)
        
        # Set default values
        self.hours_entry.delete(0, 'end')
        self.hours_entry.insert(0, "0")
        self.minutes_entry.delete(0, 'end')
        self.minutes_entry.insert(0, "0")
        self.seconds_entry.delete(0, 'end')
        self.seconds_entry.insert(0, "0")
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg='#1a1a2e')
        buttons_frame.pack(pady=30)
        
        # Start button - GREEN
        self.start_btn = tk.Button(buttons_frame, text="START", font=("Arial", 14, "bold"),
                                   bg='#10b981', fg='white', width=10, height=1,
                                   command=self.start_timer, borderwidth=0)
        self.start_btn.grid(row=0, column=0, padx=10)
        
        # Pause button - AMBER (hidden)
        self.pause_btn = tk.Button(buttons_frame, text="PAUSE", font=("Arial", 14, "bold"),
                                   bg='#f59e0b', fg='white', width=10, height=1,
                                   command=self.pause_timer, borderwidth=0)
        self.pause_btn.grid(row=0, column=0, padx=10)
        self.pause_btn.grid_remove()
        
        # Reset button - GRAY
        self.reset_btn = tk.Button(buttons_frame, text="RESET", font=("Arial", 14, "bold"),
                                   bg='#4b5563', fg='white', width=10, height=1,
                                   command=self.reset_timer, borderwidth=0)
        self.reset_btn.grid(row=0, column=1, padx=10)
        
    def get_total_seconds(self):
        try:
            h = int(self.hours_entry.get()) if self.hours_entry.get() else 0
            m = int(self.minutes_entry.get()) if self.minutes_entry.get() else 0
            s = int(self.seconds_entry.get()) if self.seconds_entry.get() else 0
            return h * 3600 + m * 60 + s
        except:
            return 0
            
    def format_time(self, total_seconds):
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"
        
    def start_timer(self):
        if self.is_paused:
            self.resume_timer()
            return
            
        total = self.get_total_seconds()
        if total <= 0:
            self.status_label.config(text="Please enter a time!", fg='#ef4444')
            return
        
        self.initial_seconds = total
        self.remaining_seconds = total
        self.is_running = True
        self.is_paused = False
        self.stop_event.clear()
        
        # Disable entries
        self.hours_entry.config(state='disabled')
        self.minutes_entry.config(state='disabled')
        self.seconds_entry.config(state='disabled')
        
        # Switch buttons
        self.start_btn.grid_remove()
        self.pause_btn.grid()
        
        self.status_label.config(text="Running...", fg='#10b981')
        
        # Start countdown
        self.timer_thread = threading.Thread(target=self.countdown, daemon=True)
        self.timer_thread.start()
        
    def pause_timer(self):
        if self.is_running and not self.is_paused:
            self.is_paused = True
            self.pause_btn.config(text="RESUME")
            self.status_label.config(text="Paused", fg='#f59e0b')
        elif self.is_paused:
            self.resume_timer()
            
    def resume_timer(self):
        if self.is_paused:
            self.is_paused = False
            self.pause_btn.config(text="PAUSE")
            self.status_label.config(text="Running...", fg='#10b981')
            self.timer_thread = threading.Thread(target=self.countdown, daemon=True)
            self.timer_thread.start()
            
    def reset_timer(self):
        self.stop_event.set()
        time.sleep(0.2)
        
        self.is_running = False
        self.is_paused = False
        
        # Re-enable entries
        self.hours_entry.config(state='normal')
        self.minutes_entry.config(state='normal')
        self.seconds_entry.config(state='normal')
        
        # Reset buttons
        self.pause_btn.grid_remove()
        self.start_btn.grid()
        
        if self.initial_seconds > 0:
            self.remaining_seconds = self.initial_seconds
            self.timer_label.config(text=self.format_time(self.remaining_seconds))
        
        self.status_label.config(text="Ready", fg='#a0a0a0')
        
    def countdown(self):
        while self.remaining_seconds > 0 and not self.stop_event.is_set():
            if not self.is_paused:
                time.sleep(1)
                if not self.stop_event.is_set() and not self.is_paused:
                    self.remaining_seconds -= 1
                    self.root.after(0, self.update_display)
            else:
                time.sleep(0.1)
        
        if not self.stop_event.is_set():
            self.root.after(0, self.timer_complete)
            
    def update_display(self):
        self.timer_label.config(text=self.format_time(self.remaining_seconds))
        
    def timer_complete(self):
        self.is_running = False
        self.remaining_seconds = 0
        self.timer_label.config(text="00:00:00")
        self.timer_label.config(fg='#22d3ee')
        self.status_label.config(text="Time's up!", fg='#22d3ee')
        
        # Flash effect
        def flash(count=0):
            if count < 6:
                color = '#22d3ee' if count % 2 == 0 else 'white'
                self.timer_label.config(fg=color)
                self.root.after(300, lambda: flash(count + 1))
            else:
                self.timer_label.config(fg='white')
                # Re-enable entries
                self.hours_entry.config(state='normal')
                self.minutes_entry.config(state='normal')
                self.seconds_entry.config(state='normal')
                self.pause_btn.grid_remove()
                self.start_btn.grid()
        
        flash()


def main():
    root = tk.Tk()
    app = CountdownTimerApp(root)
    
    def on_closing():
        app.stop_event.set()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
