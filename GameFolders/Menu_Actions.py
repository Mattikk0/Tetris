import tkinter as tk
import pygame as pg
import Main_Game

set_delay = 500
automatic = False
if not hasattr(tk, '_default_root'):
    root = tk.Tk()
    root.withdraw()


def on_close():
    exit(0)
def validate_input(new_value):
    return new_value.isdigit() and len(new_value) <= 4 or new_value == ""

def start_game(delay_val, delay_check_val):
    global root
    global set_delay
    global automatic
    if delay_val != '':
        set_delay = int(delay_val)
    else:
        set_delay = 500
    if delay_check_val:
        automatic = True
    root.destroy()
    root.quit()
def launch_menu():
    global root
    root = tk.Tk()
    delay_check_var = tk.BooleanVar(value=False)
    delay = tk.Frame(root)
    delay.pack(pady=5, fill="x")
    window_width = 500
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    vcmd = (root.register(validate_input), "%P")

    delay_label = tk.Label(delay, text="Delay (in ms, default: 500ms): ", font=("Arial", 10), fg="black")
    delay_label.pack(pady=10)
    entry = tk.Entry(delay, validate="key", validatecommand=vcmd)
    entry.pack()
    delay_checkbox = tk.Checkbutton(delay, text="Automatically ascending", variable=delay_check_var, font=("Arial", 10))
    delay_checkbox.pack(side='left', expand=True, pady=10)

    start_game_button = tk.Button(root, text="Start",width=20, height=2, command=lambda: start_game(entry.get(), delay_check_var.get()))
    start_game_button.pack(side='left', expand=True, padx=1)
    root.bind("<Return>", lambda event: start_game(entry.get(), delay_check_var.get()))

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
