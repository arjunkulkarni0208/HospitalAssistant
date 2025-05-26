from tkinter import Tk, Frame, Button, Label, Scrollbar, Canvas, BOTH, RIGHT, Y, LEFT, NW
import shared_data
import os  # For executing next script

# Urology FAQ data
faq_data = {
    "Urinary Issues": {
        "Frequent Urination": "Frequent urination can result from urinary tract infections, overactive bladder, or diabetes.",
        "Painful Urination": "Pain during urination is often due to infections, inflammations, or stones in the urinary tract.",
        "Blood in Urine": "Blood in urine can indicate infections, stones, or more serious conditions like cancer.",
        "Urinary Incontinence": "It can be due to weakened pelvic muscles, nerve damage, or prostate issues.",
        "Urgency and Frequency": "This may be due to infections, overactive bladder, or interstitial cystitis."
    },
    "Kidney and Bladder Health": {
        "Kidney Stones": "Symptoms include severe back or side pain, blood in urine, and nausea.",
        "Bladder Infections": "Typically treated with antibiotics and increased fluid intake.",
        "Overactive Bladder": "A condition where there's a frequent urge to urinate, often with leakage.",
        "Interstitial Cystitis": "A chronic bladder condition causing bladder pressure and pain.",
        "Bladder Stones": "They develop from concentrated urine, leading to crystal formation."
    },
    "Prostate Health": {
        "Enlarged Prostate (BPH)": "Benign Prostatic Hyperplasia is a non-cancerous enlargement of the prostate gland.",
        "Prostatitis": "It can be due to bacterial infections or other unknown causes.",
        "Prostate Cancer": "Risk factors include age, family history, and certain genetic factors.",
        "PSA Testing": "A blood test measuring prostate-specific antigen levels to screen for prostate issues.",
        "Prostate Surgery": "Required for severe BPH or prostate cancer not manageable with other treatments."
    },
    "Men’s Sexual Health": {
        "Erectile Dysfunction": "Factors include stress, medical conditions, or medications.",
        "Low Testosterone": "Signs include fatigue, decreased libido, and mood changes.",
        "Male Infertility": "Often caused by issues with sperm production or delivery.",
        "Vasectomy": "Reversal is possible but not guaranteed.",
        "Peyronie’s Disease": "A condition causing curved, painful erections due to scar tissue."
    },
    "Women’s Urologic Health": {
        "Recurrent UTIs": "Can result from anatomy, sexual activity, or hygiene practices.",
        "Urinary Incontinence": "Treatments include pelvic floor exercises, medications, or surgery.",
        "Pelvic Organ Prolapse": "When pelvic organs drop due to weakened support muscles.",
        "Interstitial Cystitis": "Managed through diet changes, medications, and bladder training.",
        "Overactive Bladder": "Treatments include lifestyle changes, medications, and nerve therapies."
    }
}

def continue_to_next_stage():
    # Replace with your actual next stage script
    os.system("python3 show_data.py")  # Change to your next script

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
    root.title("Urology FAQ")
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

    Label(content_frame, text="Select a Urology Category", font=("Arial", 24, "bold"),
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

