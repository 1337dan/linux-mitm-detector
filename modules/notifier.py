# modules/notifier.py

import os
import platform

def alert(title, message):
    """
    Sends an alert to the user via terminal and (if available) GUI desktop notification.
    """
    # Always print to terminal
    print(f"\n[ALERT] {title}: {message}\n")

    # Only try GUI notification if running in a graphical desktop
    if "DISPLAY" in os.environ and platform.system() == "Linux":
        try:
            # notify-send is built-in on most Linux desktops
            os.system(f'notify-send "{title}" "{message}"')
        except Exception as e:
            print(f"[!] Failed to send GUI notification: {e}")
