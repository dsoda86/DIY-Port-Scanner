from colorama import Fore, Style
import pyfiglet
import sys
import socket
import threading
from datetime import datetime

# Define colorama colors and styles
RESET = Style.RESET_ALL
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
YELLOW = Fore.YELLOW
BRIGHT = Style.BRIGHT


# ASCII Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
ascii_banner_colored = f"{YELLOW}{BRIGHT}{ascii_banner}{RESET}"
print(ascii_banner_colored)

# Get Target IP from user input
target = input(f"{BRIGHT}Please Enter the Target IP: {RESET}").strip()

# Validate target input
try:
    target = socket.gethostbyname(target) #Convert hostname to IP

except socket.gaierror:
        print("\nHostname Could Not Be Resolved! ❌")
        sys.exit()

except socket.error:
        print("\nHost Not Responding! ⛔")
        sys.exit()

# Banner
print("_" * 100)
print(f"{BRIGHT}Scanning Target:{RESET} {target}")
print(f"{BRIGHT}Scanning started at:{RESET} {datetime.now()}")
print("_" * 100)

#Defined dictionary for port numbers, their services, and a short description
common_ports = {
    7: {"service": "Echo", "description": "Echo service - Used for testing and debugging"},
    20: {"service": "FTP-Data", "description": "File Transfer Protocol (FTP) - Data transfer"},
    21: {"service": "FTP", "description": "File Transfer Protocol (FTP) - Control connection"},
    22: {"service": "SSH", "description": "Secure Shell - Remote logins, file transfers (scp, sftp), and port forwarding"},
    23: {"service": "Telnet", "description": "Unsecured text-based remote login"},
    25: {"service": "SMTP", "description": "Simple Mail Transfer Protocol - Sending emails"},
    53: {"service": "DNS", "description": "Domain Name System - Resolves domain names to IP addresses"},
    67: {"service": "DHCP", "description": "Dynamic Host Configuration Protocol - Assigns IP addresses to devices"},
    68: {"service": "DHCP", "description": "Client-side DHCP service"},
    69: {"service": "TFTP", "description": "Trivial File Transfer Protocol - Simplified FTP with no authentication"},
    80: {"service": "HTTP", "description": "HyperText Transfer Protocol - Web traffic"},
    88: {"service": "Kerberos", "description": "Authentication protocol for secure identity verification"},
    102: {"service": "MS Exchange", "description": "Microsoft Exchange messaging service"},
    110: {"service": "POP3", "description": "Post Office Protocol v3 - Email receiving"},
    135: {"service": "RPC", "description": "Microsoft Remote Procedure Call - Used for Windows services"},
    137: {"service": "NetBIOS-NS", "description": "NetBIOS Name Service - Resolves NetBIOS names"},
    139: {"service": "NetBIOS-SSN", "description": "NetBIOS Session Service - Windows file sharing"},
    143: {"service": "IMAP", "description": "Internet Message Access Protocol - Email retrieval"},
    381: {"service": "HP OpenView", "description": "HP OpenView Network Node Manager"},
    383: {"service": "HP OpenView", "description": "HP OpenView Performance Agent"},
    389: {"service": "LDAP", "description": "Lightweight Directory Access Protocol - Directory services"},
    443: {"service": "HTTPS", "description": "Secure web traffic (TLS/SSL)"},
    445: {"service": "Microsoft-DS", "description": "Microsoft Directory Services - Windows file sharing"},
    464: {"service": "Kerberos", "description": "Kerberos authentication (password changes)"},
    465: {"service": "SMTPS", "description": "Secure SMTP - Email sending with encryption"},
    587: {"service": "SMTP", "description": "Email submission port for sending messages"},
    593: {"service": "RPC", "description": "Microsoft RPC over HTTP"},
    636: {"service": "LDAPS", "description": "Secure LDAP (SSL/TLS)"},
    691: {"service": "MS Exchange Routing", "description": "Microsoft Exchange email routing"},
    902: {"service": "VMware Server", "description": "VMware remote management"},
    989: {"service": "FTPS", "description": "Secure FTP (data channel)"},
    990: {"service": "FTPS", "description": "Secure FTP (control channel)"},
    993: {"service": "IMAPS", "description": "Secure IMAP for email retrieval"},
    995: {"service": "POP3S", "description": "Secure POP3 for email retrieval"},
    1025: {"service": "Microsoft RPC", "description": "Remote procedure call for Windows services"},
    1194: {"service": "OpenVPN", "description": "OpenVPN secure tunneling"},
    1337: {"service": "Elite", "description": "Commonly used by hackers and gaming servers"},
    1462: {"service": "MS DCOM", "description": "Microsoft Distributed Component Object Model (DCOM) service"},
    1589: {"service": "Cisco VQP", "description": "Cisco VLAN Query Protocol"},
    1701: {"service": "L2TP", "description": "Layer 2 Tunneling Protocol for VPNs"},
    1723: {"service": "PPTP", "description": "Point-to-Point Tunneling Protocol for VPNs"},
    1725: {"service": "Steam", "description": "Used by Steam for gaming communication"},
    1801: {"service": "MSMQ", "description": "Microsoft Message Queuing - Message-based communication for distributed systems"},
    1812: {"service": "RADIUS", "description": "Remote Authentication Dial-In User Service - Authentication"},
    1813: {"service": "RADIUS", "description": "Remote Authentication Dial-In User Service - Accounting"},
    2082: {"service": "cPanel", "description": "Web hosting control panel (non-SSL)"},
    2083: {"service": "cPanel", "description": "Web hosting control panel (SSL)"},
    2103: {"service": "MS DCOM", "description": "Microsoft Distributed Component Object Model (DCOM) service"},
    2105: {"service": "MS DCOM", "description": "Microsoft Distributed Component Object Model (DCOM) service"},
    2107: {"service": "MS DCOM", "description": "Microsoft Distributed Component Object Model (DCOM) service"},
    2483: {"service": "Oracle DB", "description": "Oracle database listener (TCP)"},
    2484: {"service": "Oracle DB", "description": "Oracle database listener (SSL)"},
    2967: {"service": "Symantec AV", "description": "Symantec AntiVirus management"},
    2968: {"service": "Ensemble", "description": "Used for Ensemble services in Windows environments"},
    3074: {"service": "Xbox Live", "description": "Used for Xbox gaming communication"},
    3306: {"service": "MySQL", "description": "MySQL database server"},
    3724: {"service": "World of Warcraft", "description": "Used for WoW online gaming"},
    3389: {"service": "RDP", "description": "Remote Desktop Protocol - Remote access"},
    3868: {"service": "Diameter", "description": "Authentication, Authorization, and Accounting protocol"},
    4664: {"service": "Google Desktop", "description": "Used for Google Desktop Search"},
    5004: {"service": "RTP", "description": "Real-time Transport Protocol - Voice and video streaming"},
    5040: {"service": "Windows RDS", "description": "Remote Desktop Services licensing service"},
    5426: {"service": "DE-Spot", "description": "Simple network presence protocol"},
    5432: {"service": "PostgreSQL", "description": "PostgreSQL database server"},
    5900: {"service": "VNC", "description": "Virtual Network Computing - Remote desktop"},
    6881: {"service": "BitTorrent", "description": "Peer-to-peer file sharing"},
    6970: {"service": "QuickTime Streaming", "description": "Apple QuickTime media streaming"},
    6999: {"service": "BitTorrent", "description": "Additional BitTorrent service port"},
    8080: {"service": "HTTP Proxy", "description": "Alternative HTTP port for web proxies"},
    8086: {"service": "InfluxDB", "description": "Time-series database HTTP API"},
    8087: {"service": "Proxy", "description": "Alternative HTTP proxy service"},
    8222: {"service": "VMware", "description": "VMware Server Web Access"},
    8443: {"service": "HTTPS-Alt", "description": "Alternative HTTPS port often used for admin panels and web services"},
    8834: {"service": "Nessus", "description": "Tenable Nessus vulnerability scanner web interface"},
    8845: {"service": "Google Talk", "description": "Google Talk VoIP service"},
    9100: {"service": "JetDirect", "description": "HP printer network service"},
    10000: {"service": "Webmin", "description": "Web-based Linux server management"},
    12345: {"service": "NetBus", "description": "Common backdoor Trojan port"},
    13331: {"service": "Backdoor Bifrost", "description": "Possible Trojan/Backdoor malware port"},
    13344: {"service": "Backdoor Bifrost", "description": "Possible Trojan/Backdoor malware port"},
    14622: {"service": "Unassigned", "description": "No well-known assignment"},
    27017: {"service": "MongoDB", "description": "MongoDB database service"},
    27374: {"service": "Sub7", "description": "Common backdoor Trojan port"},
    31337: {"service": "Elite", "description": "Hacker-related port (used in old exploits)"},
    32682: {"service": "Unassigned", "description": "No well-known assignment"},
    33060: {"service": "MySQLX", "description": "MySQL X protocol - Used for document store and NoSQL features"},
    49664: {"service": "Dynamic RPC", "description": "Microsoft dynamic RPC service port"},
    49665: {"service": "Dynamic RPC", "description": "Microsoft dynamic RPC service port"},
    49666: {"service": "Dynamic RPC", "description": "Microsoft dynamic RPC service port"},
    49667: {"service": "Dynamic RPC", "description": "Microsoft dynamic RPC service port"},
    49668: {"service": "Dynamic RPC", "description": "Microsoft dynamic RPC service port"},
    49669: {"service": "Dynamic RPC", "description": "Microsoft dynamic RPC service port"},
    49670: {"service": "Dynamic RPC", "description": "Microsoft dynamic RPC service port"},
    49671: {"service": "Dynamic RPC", "description": "Microsoft dynamic RPC service port"},
    49680: {"service": "Dynamic RPC", "description": "Microsoft dynamic RPC service port"},
    53977: {"service": "Unassigned", "description": "No well-known assignment-may be used dynamically"},
    54037: {"service": "Unassigned", "description": "No well-known assignment-may be used dynamically"},
    54235: {"service": "Unassigned", "description": "No well-known assignment-may be used dynamically"},
    59579: {"service": "Unassigned", "description": "No well-known assignment-may be used dynamically"},
    65001: {"service": "Unassigned", "description": "No well-known assignment-may be used dynamically"},
    65444: {"service": "Unassigned", "description": "No well-known assignment-may be used dynamically"}
}

# Function to scan a single port
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout to prevent hanging
        result = s.connect_ex((target, port))
        if result == 0:
            port_info = common_ports.get(port, {"service": "Unknown Service", "description": "No description available"})
            print(f"[📡] Port {CYAN}{port}{RESET} ({MAGENTA}{port_info['service']}{RESET}) ✅ - {BRIGHT}{port_info['description']}{RESET}")
            s.close()
            
    except socket.error:
         print(f"\nHost {target} is not responding! ⛔")
         sys.exit()

    except Exception as e:
         print(f"\n Error scanning {port}: {e}")

# Multithreading for faster
threads = []
try:
    for port in range(1, 65535):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

        # Limit active threads to avoid excessive system load
        if len(threads) >= 500:  
            for t in threads:
                t.join()
            threads = []

    # Ensure all threads finish
    for t in threads:
        t.join()

except KeyboardInterrupt:
        print("\nApplication Interrupted. Exiting... 💨🚪")
        sys.exit()

print("\nScanning Complete! 🚀🔥")