import time
import random
import keyboard as key
import tkinter as tk
from threading import Thread, Event
from queue import Queue
import ctypes
from styles import button_style, label_style, MAIN_BG

# Constants
KEY_MAP = {
    'w': 0x57,
    'a': 0x41,
    's': 0x53,
    'd': 0x44
}
DIRECTION_KEYS = list(KEY_MAP.keys()) + ['up']

class AntiAfkBot:
    def __init__(self):
        self.running = False
        self.event = Event()
        self.message_queue = Queue()

    def log(self, message):
        self.message_queue.put(message)

    def press_key(self, key_char):
        try:
            key_code = KEY_MAP.get(key_char)
            if key_code:
                ctypes.windll.user32.keybd_event(key_code, 0, 0, 0)
                time.sleep(random.uniform(1, 5))
                ctypes.windll.user32.keybd_event(key_code, 0, 2, 0)
        except Exception as e:
            self.log(f"Key press error: {e}")

    def open_phone(self):
        if not self.running:
            return
        wait_time = random.uniform(1, 90)
        self.log(f"Opening phone for {wait_time:.2f} seconds")
        key.send('up')
        time.sleep(wait_time)
        key.send('down')

    def bot_logic(self):
        while self.running:
            cycles = random.randint(1, 8)
            self.log(f"Running {cycles} cycles")
            for _ in range(cycles):
                if not self.running:
                    return
                key_to_press = random.choice(DIRECTION_KEYS)
                if key_to_press == 'up':
                    self.open_phone()
                else:
                    self.press_key(key_to_press)
            cycle_wait = random.uniform(60, 120)
            self.log(f"Next cycle in {cycle_wait:.2f} seconds")
            self.event.wait(cycle_wait)
            self.event.clear()

class AntiafkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Anti AFK")
        self.root.geometry("500x150")
        self.root.resizable(False, False)
        self.root.configure(bg=MAIN_BG)

        self.bot = AntiAfkBot()
        self.bot_thread = None

        self.setup_ui()
        self.check_messages()

    def setup_ui(self):
        main_container = tk.Frame(self.root, bg=MAIN_BG)
        main_container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        center_frame = tk.Frame(main_container, bg=MAIN_BG)
        center_frame.pack(expand=True)

        self.status_label = tk.Label(center_frame, text="Status: Inactive", **label_style)
        self.status_label.pack(pady=(0, 15))

        button_frame = tk.Frame(center_frame, bg=MAIN_BG)
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Start", command=self.start_bot, **button_style)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_bot, **button_style)
        self.stop_button.pack(side=tk.LEFT, padx=10)

    def check_messages(self):
        while not self.bot.message_queue.empty():
            print(self.bot.message_queue.get())
        self.root.after(100, self.check_messages)

    def start_bot(self):
        if not self.bot.running:
            self.bot.running = True
            self.bot.event = Event()
            self.bot_thread = Thread(target=self.bot.bot_logic, daemon=True)
            self.bot_thread.start()
            self.bot.log("Bot started")
            self.status_label.config(text="Status: Active")

    def stop_bot(self):
        if self.bot.running:
            self.bot.running = False
            self.bot.event.set()
            if self.bot_thread and self.bot_thread.is_alive():
                self.bot_thread.join(timeout=1)
            self.bot.log("Bot stopped")
            self.status_label.config(text="Status: Inactive")
