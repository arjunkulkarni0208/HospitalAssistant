import tkinter as tk
import shared_data
import os

# Ailment-to-doctor fixed mapping
doctors = {
    "Issue with Urine": "Dr. Anagha Kulkarni",
    "Kidney related Issue": "Dr. Anagha Kulkarni",
    "Shoulder injury/pain": "Dr. Aashay Kekatpure",
    "Elbow injury/pain": "Dr. Aashay Kekatpure",
    "Knee injury/pain": "Dr. Aashay Kekatpure",
    "Other": "(Kindly consult directly to the doctor)"
}

ailments_list = list(doctors.keys())
checkbox_vars = []

def show_doctor():
    shared_data.selected_ailments.clear()

    for var, ailment in zip(checkbox_vars, ailments_list):
        if var.get():
            shared_data.selected_ailments.append(ailment)

    if not shared_data.selected_ailments:
        lbl_doctor.config(text="Please select at least one ailment.")
        return

    # Assign doctor based on the first ailment selected
    first_ailment = shared_data.selected_ailments[0]
    shared_data.assigned_doctor = doctors.get(first_ailment, "General Physician")

    lbl_doctor.config(text=f"Suggested Doctor: {shared_data.assigned_doctor}")

    # Proceed to appropriate next screen after short delay
    root.after(3000, launch_next_stage)

def launch_next_stage():
    root.destroy()
    if shared_data.assigned_doctor == "Dr. Aashay Kekatpure":
        os.system("python3 ortho_faq.py")
    elif shared_data.assigned_doctor == "Dr. Anagha Kulkarni":
        os.system("python3 uro_faq.py")
    else:
        import show_data

# UI setup
root = tk.Tk()
root.title("Ailment Selection")
root.attributes('-fullscreen', True)
root.configure(bg=shared_data.BG_COLOR)

title = tk.Label(
    root,
    text="Select Ailments" if shared_data.selected_language == "English" else "बीमारियाँ चुनें",
    font=("Arial", 28),
    bg=shared_data.BG_COLOR
)
title.pack(pady=30)

# Checkboxes
for ailment in ailments_list:
    var = tk.BooleanVar()
    cb = tk.Checkbutton(
        root, text=ailment, variable=var,
        font=("Arial", 20), bg=shared_data.BG_COLOR
    )
    cb.pack(anchor="w", padx=50)
    checkbox_vars.append(var)

btn = tk.Button(root, text="Get Doctor Suggestion", font=("Arial", 22), command=show_doctor)
btn.pack(pady=30)

lbl_doctor = tk.Label(root, text="", font=("Arial", 22), fg="green", bg=shared_data.BG_COLOR)
lbl_doctor.pack()

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

root.mainloop()

