import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Localhost for testing
    common_ports = [21, 22, 80, 443, 3306]
    scan_ports(target_ip, common_ports)
