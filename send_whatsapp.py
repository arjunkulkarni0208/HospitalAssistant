import pywhatkit
import time
import shared_data

# Hardcoded numbers with country code (modify as needed)
patient_number = "+919607379080"
hospital_number = "+919766479480"

def build_summary_message():
    info = f"""
🧾 *Patient Summary* 🏥

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

    info += "\n\nSent via Hospital Assistant 🤖"

    return info.strip()

def send_summary_via_whatsapp(number, message):
    try:
        print(f"📤 Sending to: {number}")
        pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
        print("✅ Message sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send message to {number}: {e}")

if __name__ == "__main__":
    print("Works")
    message = build_summary_message()
    
    send_summary_via_whatsapp(patient_number, message)
    time.sleep(20)  # Delay to prevent WhatsApp from blocking second message
    send_summary_via_whatsapp(hospital_number, message)
