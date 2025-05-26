import tkinter as tk
import shared_data
import time

def show_wait_screen():
    wait_root = tk.Toplevel(root)
    wait_root.attributes('-fullscreen', True)
    wait_root.configure(bg='black')  # background for contrast
    wait_label = tk.Label(
        wait_root,
        text="Please wait while we send your report.\nकृपया प्रतीक्षा करें, आपकी रिपोर्ट भेजी जा रही है।\n\n*DO NOT CLICK ANYTHING / कृपया कुछ भी क्लिक न करें*",
        font=("Arial", 24),
        fg="white",
        bg="black",
        justify="center",
        wraplength=1000
    )
    wait_label.pack(expand=True)
    wait_root.update()
    time.sleep(6)

    import send_text  # your WhatsApp sending code

    wait_root.destroy()  # close wait screen after message is sent

  # import run  # Step 5: move to chatbot

def send_text():
    show_wait_screen()
    root.destroy()

root = tk.Tk()
root.title("Summary")
root.attributes('-fullscreen', True)
root.configure(bg=shared_data.BG_COLOR)

title = tk.Label(root, text="Patient Summary", font=("Arial", 20), bg=shared_data.BG_COLOR)
title.pack(pady=25)

info = f"""
Language: {shared_data.selected_language}
Name: {shared_data.patient_name}
Age: {shared_data.patient_age}
Phone: {shared_data.patient_phone}

--- Health Test Results ---
"""
for key, value in shared_data.health_data.items():
    info += f"{key}: {value}\n"

info += "\n--- Reported Ailments ---\n"
info += ", ".join(shared_data.selected_ailments)

info += f"\n\n--- Suggested Doctor ---\n{shared_data.assigned_doctor}"

lbl_info = tk.Label(root, text=info, font=("Arial", 16), justify="left", bg=shared_data.BG_COLOR)
lbl_info.pack(padx=50, pady=5)

btn = tk.Button(root, text="Continue", font=("Arial", 14), command=send_text)
btn.pack(pady=15)

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

root.mainloop()

