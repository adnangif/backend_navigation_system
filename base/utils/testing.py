import socket

def scan_for_esp32():
    esp32_devices = []
    # Define the IP range to scan, adjust as needed
    ip_range = "192.168.1."
    # Define the port that ESP32 devices commonly use (adjust if needed)
    port = 80  

    for i in range(1, 255):
        ip = ip_range + str(i)
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)  # Set timeout for connection attempt
            # Attempt to connect to the IP address and port
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"ESP32 found at IP address: {ip}")
                esp32_devices.append(ip)
            sock.close()
        except socket.error:
            pass

    return esp32_devices

if __name__ == "__main__":
    esp32_devices = scan_for_esp32()
    if not esp32_devices:
        print("No ESP32 devices found on the network.")
