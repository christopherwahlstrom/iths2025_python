# Praktisk uppgift 4

print ("---Praktisk uppgift 4: Pentest data ---")

#1 Skapa en variabel target_ip med en IP-adress.
target_ip = "192.168.1.10"

#2 Skapa en variabel open_ports som är en lista med

open_ports = [22, 80 , 443]

#3. Skapa en variabel vulnerable med ett booleskt värde.

vulnerable = True

#4. Skriv ut värdena och deras datatyper.

print("Target IP:", target_ip, "Type:", type(target_ip))
print("Open Ports:", open_ports, "Type:", type(open_ports))
print("Vulnerable:", vulnerable, "Type:", type(vulnerable))


