# modules/arp_detector.py

import os
import time
import subprocess
from modules import notifier, logger

# Store initial (legitimate) gateway MAC
known_gateway_mac = None

def get_gateway_ip():
    """
    Get the current default gateway IP using 'ip route' command.
    """
    try:
        route_output = subprocess.check_output("ip route", shell=True).decode()
        for line in route_output.split('\n'):
            if line.startswith('default'):
                return line.split()[2]
    except Exception as e:
        print(f"[ERROR] Failed to get gateway IP: {e}")
    return None
    
from scapy.all import ARP, Ether, srp

def get_mac_from_arp(ip):
    """
    Uses Scapy to send an ARP request and return the MAC address.
    """
    try:
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
        ans, _ = srp(pkt, timeout=2, verbose=0)
        for sent, received in ans:
            return received.hwsrc
    except Exception as e:
        print(f"[ERROR] Scapy failed to get MAC: {e}")
    return None


def run():
    """
    Continuously monitor the gateway MAC address and detect changes.
    """
    global known_gateway_mac

    print("[ARP Detector] Starting ARP spoofing detection...")

    gateway_ip = get_gateway_ip()
    if not gateway_ip:
        print("[!] Could not determine gateway IP. Exiting ARP module.")
        return

    print(f"[+] Gateway IP: {gateway_ip}")

    known_gateway_mac = get_mac_from_arp(gateway_ip)
    if not known_gateway_mac:
        print("[!] Could not determine initial MAC. Exiting ARP module.")
        return

    print(f"[+] Initial Gateway MAC: {known_gateway_mac}")

    while True:
        current_mac = get_mac_from_arp(gateway_ip)
        if current_mac and current_mac != known_gateway_mac:
            alert_msg = f"⚠️ Possible ARP spoofing detected! Gateway MAC changed from {known_gateway_mac} to {current_mac}"
            print(alert_msg)
            notifier.alert("MITM ALERT", alert_msg)
            logger.log_event("ARP Spoofing", gateway_ip, current_mac)
        time.sleep(5)  # Check every 5 seconds
