# modules/logger.py

import os
from datetime import datetime

# Define the log file path
LOG_FILE = os.path.expanduser("~/mitm_tool_logs.txt")

def log_event(attack_type, target_ip, target_mac):
    """
    Log an event with details like attack type, IP, MAC, and timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{attack_type}] Target IP: {target_ip}, MAC: {target_mac}\n"

    try:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(entry)
    except Exception as e:
        print(f"[!] Failed to write log: {e}")

def show_recent_logs(count=10):
    """
    Display the last `count` log entries from the log file.
    """
    print(f"\n[+] Showing last {count} logs from {LOG_FILE}...\n")

    if not os.path.exists(LOG_FILE):
        print("[!] No logs found yet.")
        return

    try:
        with open(LOG_FILE, "r") as log_file:
            lines = log_file.readlines()
            for line in lines[-count:]:
                print(line.strip())
    except Exception as e:
        print(f"[!] Failed to read log file: {e}")
