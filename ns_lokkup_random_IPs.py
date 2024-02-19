import socket
import time
import random

def continuous_nslookup():
    while True:
        # Generate a random IP address (for demonstration purposes)
        ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))

        try:
            # Perform DNS lookup
            hostname, _, _ = socket.gethostbyaddr(ip_address)
            print(f"IP Address: {ip_address} resolves to Hostname: {hostname}")
        except socket.herror as e:
            print(f"Error for IP Address {ip_address}: {e}")

        # Wait for some time before the next lookup
        time.sleep(1)

if __name__ == "__main__":
    continuous_nslookup()
