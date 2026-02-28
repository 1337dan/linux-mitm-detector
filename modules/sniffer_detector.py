# modules/sniffer_detector.py

from scapy.all import ARP, Ether, srp
import time
import random
from modules import notifier, logger

def generate_fake_mac():
    # Generate a random unicast MAC address
    return "02:" + ":".join(f"{random.randint(0, 255):02x}" for _ in range(5))

def detect_sniffers(interface="eth0"):
    """
    Send a unicast ARP request with a fake destination MAC.
    Devices in promiscuous mode might respond even though it's not for them.
    """

    fake_ip = "192.168.100.250"  # Nonexistent IP
    fake_mac = generate_fake_mac()

    print(f"[Sniffer Detector] Scanning for sniffers on {interface}...")

    # Send a unicast packet to a fake MAC and fake IP
    ether = Ether(dst=fake_mac)
    arp = ARP(pdst=fake_ip)
    packet = ether / arp

    ans, _ = srp(packet, timeout=3, iface=interface, verbose=0)

    for sent, received in ans:
        alert_msg = (
            f"⚠️ Promiscuous mode detected! Host {received.psrc} "
            f"responded to unicast probe for {fake_ip}. MAC: {received.hwsrc}"
        )
        print(alert_msg)
        notifier.alert("Sniffer Detected", alert_msg)
        logger.log_event("Sniffing Detection", received.psrc, received.hwsrc)

def run():
    """
    Main loop for sniffer detection — runs every 30 seconds.
    """
    interface = "eth0"  # Change if needed (e.g., wlan0)
    while True:
        detect_sniffers(interface)
        time.sleep(30)
