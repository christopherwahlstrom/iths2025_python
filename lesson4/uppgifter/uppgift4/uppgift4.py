# pylint: disable=missing-module-docstring

import os
import platform

# Ip pinger
# Lägg till IP-adresser i en text fil (en ip-adress per rad).
# Öppna filen och pinga varje ip-adress. Skriv ut resultatet till terminalen
# och till en fil.

def ping_ip(ip):
    if platform.system().lower() == "windows":
        response = os.system(f"ping -n 1 {ip} > NUL 2>&1")
    else:
        response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    return response

# Skapa en fil med IP-adresser om den inte finns (för test)
if not os.path.exists("ips.txt"):
    with open("ips.txt", "w") as f:
        f.write("127.0.0.1\n")
        f.write("8.8.8.8\n")
        f.write("10.0.0.99\n")
        f.write("192.168.1.1\n")


with open("ips.txt", "r") as file:
    ips = file.read().splitlines()

with open("ping_results.txt", "w") as results:
    for ip in ips:
        if ping_ip(ip) == 0:
            result = f"{ip} is available"
        else:
            result = f"{ip} is unavailable"
        
        print(result)
        results.write(result + "\n")
