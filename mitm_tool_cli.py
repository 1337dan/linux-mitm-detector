#!/usr/bin/env python3

import time
from modules import arp_detector, sniffer_detector, ssl_checker, notifier, logger

def banner():
    """
    Displays the custom MITM DETECTOR ASCII logo.
    """
    print(r"""
 /$$      /$$ /$$$$$$ /$$$$$$$$ /$$      /$$       /$$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$ 
| $$$    /$$$|_  $$_/|__  $$__/| $$$    /$$$      | $$__  $$| $$_____/|__  $$__/| $$_____/ /$$__  $$|__  $$__//$$__  $$| $$__  $$
| $$$$  /$$$$  | $$     | $$   | $$$$  /$$$$      | $$  \ $$| $$         | $$   | $$      | $$  \__/   | $$  | $$  \ $$| $$  \ $$
| $$ $$/$$ $$  | $$     | $$   | $$ $$/$$ $$      | $$  | $$| $$$$$      | $$   | $$$$$   | $$         | $$  | $$  | $$| $$$$$$$/
| $$  $$$| $$  | $$     | $$   | $$  $$$| $$      | $$  | $$| $$__/      | $$   | $$__/   | $$         | $$  | $$  | $$| $$__  $$
| $$\  $ | $$  | $$     | $$   | $$\  $ | $$      | $$  | $$| $$         | $$   | $$      | $$    $$   | $$  | $$  | $$| $$  \ $$
| $$ \/  | $$ /$$$$$$   | $$   | $$ \/  | $$      | $$$$$$$/| $$$$$$$$   | $$   | $$$$$$$$|  $$$$$$/   | $$  |  $$$$$$/| $$  | $$
|__/     |__/|______/   |__/   |__/     |__/      |_______/ |________/   |__/   |________/ \______/    |__/   \______/ |__/  |__/

MITM DETECTOR - Command-Line Interface
Made by Danyal 
""")

def show_menu():
    """
    Displays the user menu for selecting detection modules or viewing logs.
    """
    print("\nChoose an option:")
    print("[1] Start ARP Spoofing Detection")
    print("[2] Start Sniffer Detection")
    print("[3] Start SSL Certificate Check")
    print("[4] View Last 10 Logs")
    print("[5] Start All Detection Modules")
    print("[0] Exit")

def main():
    """
    Main CLI loop. Repeats menu and responds to user's input.
    """
    banner()

    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("[*] Starting ARP Spoofing Detection...\n")
            try:
                arp_detector.run()
            except KeyboardInterrupt:
                print("[!] ARP detection stopped by user.")

        elif choice == "2":
            print("[*] Starting Sniffer Detection...\n")
            try:
                sniffer_detector.run()
            except KeyboardInterrupt:
                print("[!] Sniffer detection stopped by user.")

        elif choice == "3":
            print("[*] Starting SSL Certificate Validation...\n")
            try:
                ssl_checker.run()
            except KeyboardInterrupt:
                print("[!] SSL checker stopped by user.")

        elif choice == "4":
            print("[*] Displaying last 10 logs...\n")
            logger.show_recent_logs(10)

        elif choice == "5":
            print("[*] Starting all detection modules...\n")
            try:
                arp_detector.run()
                sniffer_detector.run()
                ssl_checker.run()
            except KeyboardInterrupt:
                print("[!] All modules stopped by user.")

        elif choice == "0":
            print("[*] Exiting MITM Detector. Goodbye!")
            break

        else:
            print("[!] Invalid choice. Please enter a number from 0 to 5.")

        time.sleep(1)

# Script entry point
if __name__ == "__main__":
    main()
