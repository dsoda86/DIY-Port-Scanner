import pyfiglet
import sys
import socket
import threading
from datetime import datetime

# ASCII Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Get Target IP from user input
target = input("Please Enter the Target IP: ").strip()

# Validate target input
try:
    target = socket.gethostbyname(target) #Convert hostname to IP

except socket.gaierror:
        print("\nHostname Could Not Be Resolved! ⚠️")
        sys.exit()

except socket.error:
        print("\nHost Not Responding! ⛔")
        sys.exit()

# Banner
print("_" * 50)
print(f"Scanning Target: {target}")
print(f"Scanning started at: {datetime.now()}")
print("_" * 50)

# Function to scan a single port
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout to prevent hanging
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[🌐] Port {port} is open")
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
        print("\nApplication Interrupted. Exiting... ✌️")
        sys.exit()

print("\nScanning Complete! 🚀🔥")