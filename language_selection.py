import tkinter as tk
import shared_data

# Global variable to store selected language
selected_language = None

def set_language(lang):
    import shared_data
    shared_data.selected_language = lang
    print(f"Language selected: {lang}")
    root.destroy()
    import patient_info_form


# Initialize the main window
root = tk.Tk()
root.title("Hospital Helper Bot")
root.attributes('-fullscreen', True)
root.configure(bg=shared_data.BG_COLOR)

# Title
title = tk.Label(root, text="Start Assistant / सहायक शुरू करो", font=("Arial", 32), bg=shared_data.BG_COLOR)
title.pack(pady=100)

# English Button
btn_english = tk.Button(root, text="Start", font=("Arial", 24), width=15, height=2,
                        command=lambda: set_language("English"))
btn_english.pack(pady=20)



# Escape key to exit fullscreen
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

# Run the app
root.mainloop()
