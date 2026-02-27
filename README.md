# Linux-Based MITM Detector Tool

A lightweight Linux-based Command Line Interface (CLI) tool designed to
detect Man-In-The-Middle (MITM) attacks in real time.

This project focuses on identifying common MITM attack techniques such
as ARP Spoofing, Packet Sniffing, and SSL Certificate Manipulation
within local network environments.

------------------------------------------------------------------------

## Project Objective

The objective of this tool is to enhance network security by detecting
suspicious activities that indicate potential MITM attacks.

------------------------------------------------------------------------

## Features

-   ARP Spoofing Detection
-   Network Sniffer Detection (Promiscuous Mode Detection)
-   SSL Certificate Integrity Check
-   Real-Time Monitoring
-   Log Storage and Review System
-   Interactive CLI Interface
-   Lightweight and Linux Optimized

------------------------------------------------------------------------

## Supported Platforms

-   Kali Linux
-   Ubuntu
-   Debian-based Linux Distributions

------------------------------------------------------------------------

## Technologies Used

-   Python 3
-   Scapy
-   OpenSSL
-   Linux Networking Utilities

------------------------------------------------------------------------

## Installation

### Clone the Repository

git clone https://github.com/YOUR_USERNAME/linux-mitm-detector.git cd
linux-mitm-detector

### Install Dependencies

pip install -r requirements.txt

### Run the Tool (Root Required)

sudo python3 mitm_tool_cli.py

------------------------------------------------------------------------

## Requirements

-   Python 3.x
-   Root Privileges (required for packet inspection)
-   Scapy
-   Cryptography Library

Example requirements.txt:

scapy cryptography

------------------------------------------------------------------------

## Usage

After launching the tool, you will see:

Choose an option:

\[1\] Start ARP Spoofing Detection\
\[2\] Start Sniffer Detection\
\[3\] Start SSL Certificate Check\
\[4\] View Last 10 Logs\
\[5\] Start All Detection Modules\
\[0\] Exit

Enter your choice and the selected detection module will start
monitoring the network.

------------------------------------------------------------------------

## How It Works

### ARP Spoofing Detection

Monitors ARP table entries and detects IP-MAC inconsistencies that
indicate ARP poisoning.

### Sniffer Detection

Detects network interfaces running in promiscuous mode, which may
indicate packet sniffing attempts.

### SSL Certificate Check

Verifies SSL certificate fingerprints to detect HTTPS interception or
certificate manipulation.

------------------------------------------------------------------------

## Logs

All detection logs are stored inside the logs/ directory.

Logs include: - Timestamp - Detection Type - Alert Description -
Suspicious IP or MAC Address

------------------------------------------------------------------------

## Security and Ethical Disclaimer

This tool is developed strictly for educational and defensive
cybersecurity purposes only.

Do not use this software on networks without proper authorization. The
developer is not responsible for any misuse of this tool.

------------------------------------------------------------------------

## License

This project is licensed under the MIT License.

------------------------------------------------------------------------

## Author

Muhammad Danyal Khan

