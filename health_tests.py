import tkinter as tk
import shared_data
import time

# Mock sensor data
mock_data = {
    "Weight": "65 kg",
    "Blood Pressure": "120/80 mmHg",
    "Pulse": "76 bpm",
    "SpO2": "98%"
}

test_order = list(mock_data.keys())
current_test = 0

def next_test():
    global current_test
    if current_test >= len(test_order):
        root.destroy()
        import ailment_selection  # Step 4 (to be created)
        return

    test = test_order[current_test]
    
    result = mock_data[test]
    shared_data.health_tests[test] = result

    lbl_instruction.config(text=f"{test} Test...")
    lbl_result.config(text=f"{result}")

    current_test += 1

    # Auto advance after 2 seconds
    root.after(2000, next_test)

# GUI Setup
root = tk.Tk()
root.title("Health Check")
root.attributes('-fullscreen', True)
root.configure(bg=shared_data.BG_COLOR)

lbl_title = tk.Label(root, text="Health Tests" if shared_data.selected_language == "English" else "स्वास्थ्य परीक्षण",
                     font=("Arial", 32), bg=shared_data.BG_COLOR)
lbl_title.pack(pady=40)

lbl_instruction = tk.Label(root, text="", font=("Arial", 28), bg=shared_data.BG_COLOR)
lbl_instruction.pack(pady=20)

lbl_result = tk.Label(root, text="", font=("Arial", 26), fg="green", bg=shared_data.BG_COLOR)
lbl_result.pack(pady=20)

# Start the first test after a short delay
root.after(1000, next_test)

# Escape to exit fullscreen
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

root.mainloop()
