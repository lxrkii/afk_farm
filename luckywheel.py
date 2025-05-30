import tkinter as tk
import pyautogui
import time
import keyboard as key
from threading import Thread
from styles import button_style, label_style, entry_style, MAIN_BG

COORDINATES = {
    "FullHD": {
        "shop": (1286, 275),
        "roulette": (577, 335),
        "luckywheel": (685, 642),
        "spin": (972, 896)
    },
    "QuadHD": {
        "shop": (1600, 455),
        "roulette": (900, 515),
        "luckywheel": (1080, 825),
        "spin": (1275, 1065)
    }
}

class LuckyWheelApp:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.resolution_var = tk.StringVar(value="FullHD")

        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.root.title("Колесо удачи")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.configure(bg=MAIN_BG)

    def create_widgets(self):
        tk.Label(self.root, text="Введите количество часов (от 0 до 4):", **label_style).pack()
        self.hours_entry = tk.Entry(self.root, **entry_style, width=20)
        self.hours_entry.pack()

        tk.Label(self.root, text="Введите количество минут (от 0 до 59):", **label_style).pack()
        self.minutes_entry = tk.Entry(self.root, **entry_style, width=20)
        self.minutes_entry.pack()

        self.toggle_button = tk.Button(self.root, text="Запустить", command=self.toggle_bot, **button_style)
        self.toggle_button.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Состояние: не активно", **label_style)
        self.status_label.pack()

        self.resolution_label = tk.Label(self.root, text=f"Активное разрешение: {self.resolution_var.get()}", **label_style)
        self.resolution_label.pack()

        resolution_frame = tk.Frame(self.root, bg=MAIN_BG)
        resolution_frame.pack(pady=5)
        for res in ["FullHD", "QuadHD"]:
            tk.Button(resolution_frame, text=res, command=lambda r=res: self.set_resolution(r), **button_style).pack(side="left", padx=5)

        self.result_label = tk.Label(self.root, text="", **label_style)
        self.result_label.pack()

    def set_resolution(self, res):
        self.resolution_var.set(res)
        self.resolution_label.config(text=f"Активное разрешение: {res}")

    def toggle_bot(self):
        if self.running:
            self.running = False
            self.status_label.config(text="Состояние: не активно")
            self.toggle_button.config(text="Запустить")
            self.result_label.config(text="Процесс остановлен.")
        else:
            self.start_bot()

    def start_bot(self):
        try:
            hours = int(self.hours_entry.get() or 0)
            minutes = float(self.minutes_entry.get() or 0)
            if not (0 <= hours <= 4 and 0 <= minutes <= 59):
                raise ValueError

            self.running = True
            self.status_label.config(text="Состояние: активно")
            self.toggle_button.config(text="Остановить")
            self.result_label.config(text="Можно открыть игру...")

            total_seconds = hours * 3600 + minutes * 60 + 60
            Thread(target=self.run_bot, args=(total_seconds, self.resolution_var.get()), daemon=True).start()
        except ValueError:
            self.result_label.config(text="Пожалуйста, введите корректные числа.")

    def run_bot(self, delay, resolution):
        time.sleep(delay)
        while self.running:
            self.simulate_sequence(resolution)
            time.sleep(15000)

    def simulate_sequence(self, resolution):
        def key_cycle(k):
            key.press(k)
            time.sleep(1)
            key.release(k)

        key_cycle('f10')
        time.sleep(2)
        for action in ["shop", "roulette", "luckywheel", "spin"]:
            self.click_coordinates(COORDINATES[resolution][action])
            time.sleep(2 if action != "spin" else 40)

        for _ in range(2):
            key_cycle('esc')
            time.sleep(1)

    def click_coordinates(self, coords):
        pyautogui.click(coords[0], coords[1])
