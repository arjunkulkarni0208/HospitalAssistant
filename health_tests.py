import tkinter as tk
from tkinter import messagebox
import shared_data

def next_screen():
    shared_data.bp = bp_entry.get()
    shared_data.weight = weight_entry.get()
    shared_data.oxygen = oxygen_entry.get()

    if not (shared_data.bp and shared_data.weight and shared_data.oxygen):
        messagebox.showwarning("Input Error", "Please enter all values.")
        return

    root.destroy()
    import ailment_selection

root = tk.Tk()
root.title("Health Tests")
root.attributes('-fullscreen', True)
root.configure(bg=shared_data.BG_COLOR)

title_label = tk.Label(root, text="Enter Health Test Readings", font=("Arial", 24), bg=shared_data.BG_COLOR)
title_label.pack(pady=30)

bp_label = tk.Label(root, text="Blood Pressure (e.g., 120/80):", font=("Arial", 18), bg=shared_data.BG_COLOR)
bp_label.pack(pady=10)
bp_entry = tk.Entry(root, font=("Arial", 18))
bp_entry.pack(pady=5)

weight_label = tk.Label(root, text="Weight (kg):", font=("Arial", 18), bg=shared_data.BG_COLOR)
weight_label.pack(pady=10)
weight_entry = tk.Entry(root, font=("Arial", 18))
weight_entry.pack(pady=5)

oxygen_label = tk.Label(root, text="Oxygen Level (%):", font=("Arial", 18), bg=shared_data.BG_COLOR)
oxygen_label.pack(pady=10)
oxygen_entry = tk.Entry(root, font=("Arial", 18))
oxygen_entry.pack(pady=5)

submit_button = tk.Button(root, text="Next", font=("Arial", 18), command=next_screen)
submit_button.pack(pady=30)

root.mainloop()
