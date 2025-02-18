import pyfiglet
import sys
import socket
from datetime import datetime

# ASCII Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Get Target IP
target = input("Enter Target IP: ").strip()

# Banner
print("_" * 50)
print(f"Scanning Target: {target}")
print(f"Scanning started at: {datetime.now()}")
print("_" * 50)

# Set timeout once to speed up scanning
socket.setdefaulttimeout(0.5)

try:
    for port in range(1, 65535):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[*] Port {port} is open")

except KeyboardInterrupt:
    print("\nApplication Interrupted. Exiting... 😞")
    sys.exit()

except socket.gaierror:
    print("\nHostname Could Not Be Resolved! ❌")
    sys.exit()

except socket.error:
    print("\nHost Not Responding! 🚫")
    sys.exit()
