import pywhatkit
import time

# ─────────────────────────────────────────
#  WhatsApp Auto DM Script
#  Made with: pywhatkit
#  Requirements: pip install pywhatkit
# ─────────────────────────────────────────

# List of contacts to message
# Format: ["+91XXXXXXXXXX", "Your message here"]
contacts = [
    ["+91XXXXXXXXXX", "Hey! This is an automated message. Hope you're doing well!"],
    ["+91YYYYYYYYYY", "Hi there! Just checking in. Let me know if you need anything."],
]

def send_whatsapp_messages(contacts):
    print("Starting WhatsApp Auto DM Script...")
    print("Make sure WhatsApp Web is open in Chrome!\n")
    time.sleep(3)

    for i, contact in enumerate(contacts):
        phone_number = contact[0]
        message = contact[1]

        print(f"Sending message {i+1}/{len(contacts)} to {phone_number}...")

        try:
            # sendwhatmsg_instantly sends the message immediately
            # open_time=15 means it waits 15 seconds for WhatsApp Web to load
            pywhatkit.sendwhatmsg_instantly(
                phone_no=phone_number,
                message=message,
                wait_time=15,       # seconds to wait for WhatsApp Web to open
                tab_close=True,     # closes the tab after sending
                close_time=3        # seconds to wait before closing tab
            )

            print(f"✅ Message sent to {phone_number}")
            time.sleep(10)  # Wait 10 seconds between messages to avoid ban

        except Exception as e:
            print(f"❌ Failed to send to {phone_number}: {e}")

    print("\n✅ All messages sent successfully!")

# ─────────────────────────────────────────
# BONUS: Send a message at a specific time
# ─────────────────────────────────────────
def send_at_specific_time(phone_number, message, hour, minute):
    """
    Schedules a message at a specific time.
    hour and minute are in 24-hour format.
    Example: hour=14, minute=30 means 2:30 PM
    """
    print(f"Scheduling message to {phone_number} at {hour}:{minute:02d}...")
    pywhatkit.sendwhatmsg(
        phone_no=phone_number,
        message=message,
        time_hour=hour,
        time_min=minute,
        wait_time=15,
        tab_close=True
    )
    print("✅ Message scheduled!")


# ─────────────────────────────────────────
# RUN THE SCRIPT
# ─────────────────────────────────────────
if __name__ == "__main__":
    # Option A: Send to all contacts in the list immediately
    send_whatsapp_messages(contacts)

    # Option B: Send to one person at a specific time (uncomment to use)
    # send_at_specific_time("+91XXXXXXXXXX", "Good morning!", hour=9, minute=0)
