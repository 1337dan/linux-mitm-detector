# modules/ssl_checker.py

import ssl
import socket
from datetime import datetime
from modules import notifier, logger

# List of websites to monitor
TARGET_WEBSITES = [
    "example.com",
    "google.com",
    "github.com",
    "facebook.com"
]

def check_certificate(hostname):
    """
    Connects to the given host and retrieves the SSL certificate.
    Validates expiry date, trusted CA, and domain match.
    """
    try:
        # Connect to port 443 (HTTPS) and get certificate
        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=hostname
        )
        conn.settimeout(5)
        conn.connect((hostname, 443))
        cert = conn.getpeercert()
        conn.close()

        # Extract certificate fields
        subject = dict(x[0] for x in cert['subject'])
        issued_to = subject.get('commonName', '')
        valid_from = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
        valid_to = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")

        # Domain mismatch check
        if hostname not in issued_to:
            msg = f"⚠️ SSL CN mismatch for {hostname}! Cert issued to: {issued_to}"
            notifier.alert("SSL Warning", msg)
            logger.log_event("SSL CN Mismatch", hostname, issued_to)

        # Expired cert check
        if valid_to < datetime.utcnow():
            msg = f"⚠️ Expired certificate for {hostname}. Expired on: {valid_to}"
            notifier.alert("SSL Expired", msg)
            logger.log_event("SSL Expired", hostname, valid_to)

    except ssl.SSLCertVerificationError:
        msg = f"❌ Untrusted SSL certificate detected for {hostname}"
        notifier.alert("SSL Untrusted", msg)
        logger.log_event("SSL Untrusted Cert", hostname, "Untrusted")
    except Exception as e:
        print(f"[!] Error connecting to {hostname}: {e}")

def run():
    """
    Periodically scan known HTTPS targets for suspicious certs.
    """
    print("[SSL Checker] Starting SSL/TLS certificate analysis...")

    while True:
        for site in TARGET_WEBSITES:
            check_certificate(site)
        # Wait 5 minutes before re-checking
        import time
        time.sleep(300)

