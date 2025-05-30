import tkinter as tk
import os
import webbrowser
from PIL import Image, ImageTk
from antiafk import AntiafkApp
from builder import BuilderApp
from luckywheel import LuckyWheelApp
from styles import (
    button_style, exit_button_style,
    MAIN_BG, GREEN_ACCENT, BACKGROUND_LIGHT,
    FONT_FAMILY, FONT_SIZE
)

GITHUB_URL = "https://github.com/lxrkii"
ICON_PATH = 'icon.ico'
ICON_LINK_PATH = 'link.ico'

class AppLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Anti AFK tool by h3yad7lucjio0t6")
        self.root.geometry("200x200")
        self.root.configure(bg=MAIN_BG)

        self._set_icon()
        self._create_buttons()
        self._create_github_button()

    def _set_icon(self):
        try:
            self.root.iconbitmap(ICON_PATH)
        except tk.TclError:
            print(f"Warning: Failed to load icon: {ICON_PATH}")

    def _create_buttons(self):
        apps = [
            ("Anti-Afk", AntiafkApp),
            ("Lucky Wheel", LuckyWheelApp),
        ]

        button_frame = tk.Frame(self.root, bg=MAIN_BG)
        button_frame.pack(expand=True)

        for app_name, app_class in apps:
            tk.Button(
                button_frame, text=app_name,
                command=lambda ac=app_class: self._run_app(ac),
                **button_style
            ).pack(pady=5)

        tk.Button(
            button_frame, text="Exit",
            command=self._exit_app,
            **exit_button_style
        ).pack(pady=5)

    def _create_github_button(self):
        try:
            image = Image.open(ICON_LINK_PATH).resize((24, 24), Image.LANCZOS)
            github_icon = ImageTk.PhotoImage(image)
            button = tk.Button(
                self.root, image=github_icon,
                command=self._open_github,
                bg=MAIN_BG, activebackground=MAIN_BG,
                bd=0, relief="flat"
            )
            button.image = github_icon
        except Exception as e:
            print(f"GitHub button fallback: {e}")
            button = tk.Button(
                self.root, text="My GitHub",
                command=self._open_github,
                bg=MAIN_BG, fg=GREEN_ACCENT,
                activebackground=BACKGROUND_LIGHT,
                activeforeground=GREEN_ACCENT,
                bd=0, relief="flat",
                font=(FONT_FAMILY, FONT_SIZE - 2, "normal")
            )

        button.place(relx=0.03, rely=0.97, anchor="sw")

    def _run_app(self, app_class):
        child_root = tk.Tk()
        child_root.configure(bg=MAIN_BG)
        app_class(child_root)
        child_root.mainloop()

    def _open_github(self):
        webbrowser.open(GITHUB_URL)

    def _exit_app(self):
        self.root.destroy()
        os._exit(0)

if __name__ == "__main__":
    root = tk.Tk()
    AppLauncher(root)
    root.mainloop()
