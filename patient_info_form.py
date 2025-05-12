import tkinter as tk
import shared_data

def submit_info():
    shared_data.patient_name = entry_name.get()
    shared_data.patient_age = entry_age.get()
    shared_data.patient_phone = entry_phone.get()

    print(f"Name: {shared_data.patient_name}")
    print(f"Age: {shared_data.patient_age}")
    print(f"Phone: {shared_data.patient_phone}")

    root.destroy()
    import health_tests

root = tk.Tk()
root.title("Patient Information")
root.attributes('-fullscreen', True)
root.configure(bg=shared_data.BG_COLOR)

title = tk.Label(root, text="Enter Your Details" if shared_data.selected_language == "English" else "अपना विवरण दर्ज करें",
                 font=("Arial", 28), bg=shared_data.BG_COLOR)
title.pack(pady=40)

# Name Entry
tk.Label(root, text="Name / नाम:", font=("Arial", 20), bg=shared_data.BG_COLOR).pack(pady=10)
entry_name = tk.Entry(root, font=("Arial", 20), width=30)
entry_name.pack()

# Age Entry
tk.Label(root, text="Age / आयु:", font=("Arial", 20), bg=shared_data.BG_COLOR).pack(pady=10)
entry_age = tk.Entry(root, font=("Arial", 20), width=30)
entry_age.pack()

# Phone Number
tk.Label(root, text="Phone Number / फ़ोन नंबर:", font=("Arial", 20), bg=shared_data.BG_COLOR).pack(pady=10)
entry_phone = tk.Entry(root, font=("Arial", 20), width=30)
entry_phone.pack()

# Submit Button
tk.Button(root, text="Continue / जारी रखें", font=("Arial", 20),
          command=submit_info).pack(pady=40)

# Escape to exit fullscreen
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

root.mainloop()
