import tkinter as tk
import shared_data

def proceed_to_chatbot():
    root.destroy()
    import medical_assistant_chat  # Step 5

root = tk.Tk()
root.title("Summary")
root.attributes('-fullscreen', True)
root.configure(bg=shared_data.BG_COLOR)

title = tk.Label(root, text="Patient Summary", font=("Arial", 28), bg=shared_data.BG_COLOR)
title.pack(pady=30)

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

lbl_info = tk.Label(root, text=info, font=("Arial", 20), justify="left", bg=shared_data.BG_COLOR)
lbl_info.pack(padx=50, pady=20)

btn = tk.Button(root, text="Continue", font=("Arial", 22), command=proceed_to_chatbot)
btn.pack(pady=30)

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

root.mainloop()
