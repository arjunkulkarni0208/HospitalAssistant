from tkinter import Tk, Frame, Button, Label, Scrollbar, Canvas, BOTH, RIGHT, Y, LEFT, NW
import shared_data
import os  # For executing next script

# Orthopedics FAQ data
faq_data = {
    "Joint Pain": {
        "Knee Pain": "Knee pain can result from injury, arthritis, or overuse. Treatment may involve rest, physiotherapy, or surgery.",
        "Shoulder Pain": "Often caused by rotator cuff injuries, frozen shoulder, or bursitis.",
        "Hip Pain": "May result from arthritis, fractures, or hip impingement.",
        "Elbow Pain": "Can be due to tennis elbow, golfer’s elbow, or bursitis.",
        "Ankle Pain": "Usually from sprains, arthritis, or tendon issues."
    },
    "Fractures and Injuries": {
        "Bone Fractures": "Treatment may involve casting, bracing, or surgery depending on the type and severity.",
        "Sprains and Strains": "RICE method (Rest, Ice, Compression, Elevation) is often effective.",
        "Dislocations": "Occurs when bones are forced from their normal position; requires medical reduction.",
        "Shin Splints": "Pain along the shinbone due to overuse, common in runners.",
        "Stress Fractures": "Tiny cracks in bone often caused by repetitive force or overuse."
    },
    "Back and Spine": {
        "Lower Back Pain": "Most common orthopedic complaint; often treated with physiotherapy and pain relief.",
        "Herniated Disc": "Occurs when the soft center of a spinal disc pushes out, irritating nearby nerves.",
        "Scoliosis": "A sideways curvature of the spine that can vary from mild to severe.",
        "Sciatica": "Radiating pain along the sciatic nerve, typically down one leg.",
        "Osteoporosis": "A condition that weakens bones, making them fragile and more likely to break."
    },
    "Arthritis and Degeneration": {
        "Osteoarthritis": "Degeneration of joint cartilage and underlying bone, causing pain and stiffness.",
        "Rheumatoid Arthritis": "An autoimmune disorder affecting joints symmetrically, causing swelling and pain.",
        "Joint Replacement": "Often needed in advanced arthritis cases; common for knees and hips.",
        "Cartilage Damage": "Can be caused by injury or wear; treatments include physiotherapy or surgical repair.",
        "Joint Injections": "Steroid or hyaluronic acid injections are used to reduce joint inflammation and pain."
    }
}

def continue_to_next_stage():
    # Replace with your actual next stage script or logic
    os.system("python3 show_data.py")  # Or any other script you want

def show_answer(question, answer, content_frame, category, questions):
    for widget in content_frame.winfo_children():
        widget.destroy()

    Label(content_frame, text=question, font=("Arial", 20, "bold"),
          bg=shared_data.BG_COLOR, wraplength=1000, justify="center").pack(pady=(30, 10))
    Label(content_frame, text=answer, font=("Arial", 18),
          bg=shared_data.BG_COLOR, wraplength=1000, justify="center").pack(pady=(0, 20))

    nav_frame = Frame(content_frame, bg=shared_data.BG_COLOR)
    nav_frame.pack(pady=20)

    Button(nav_frame, text="⬅ Back", font=("Arial", 16),
           command=lambda: show_questions(category, questions, content_frame), width=12).pack(side=LEFT, padx=30)

    Button(nav_frame, text="Continue ➡", font=("Arial", 16),
           command=continue_to_next_stage, width=12).pack(side=LEFT, padx=30)

def show_questions(category, questions, content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()
    Label(content_frame, text=category, font=("Arial", 22, "bold"),
          bg=shared_data.BG_COLOR).pack(pady=20)
    for q, a in questions.items():
        Button(content_frame, text=q, font=("Arial", 16), width=60, wraplength=600,
               bg="white", command=lambda q=q, a=a: show_answer(q, a, content_frame, category, questions)).pack(pady=8)

def main():
    root = Tk()
    root.title("Orthopedic FAQ")
    root.attributes("-fullscreen", True)
    root.configure(bg=shared_data.BG_COLOR)

    canvas = Canvas(root, bg=shared_data.BG_COLOR, highlightthickness=0)
    frame = Frame(canvas, bg=shared_data.BG_COLOR)
    scrollbar = Scrollbar(root, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    canvas.create_window((0, 0), window=frame, anchor=NW)

    content_frame = Frame(frame, bg=shared_data.BG_COLOR)
    content_frame.pack()

    Label(content_frame, text="Select an Orthopedic Category", font=("Arial", 24, "bold"),
          bg=shared_data.BG_COLOR).pack(pady=30)
    for category, questions in faq_data.items():
        Button(content_frame, text=category, width=50, font=("Arial", 18),
               bg="white", command=lambda c=category, q=questions: show_questions(c, q, content_frame)).pack(pady=10)

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", on_configure)
    root.mainloop()

if __name__ == "__main__":
    main()
