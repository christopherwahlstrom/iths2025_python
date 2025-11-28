#Praktiskt uppgift 05
#Beräkna statistik från en skanning.

#1. Skapa två variabler: scanned_hosts = 50 och found_vulnerable = 8.

scanned_hosts = 50
found_vulnerable = 8

#2. Beräkna andelen sårbara maskiner(found_vulnerable / scanned_hosts * 100).

vulnerable_percentage = (found_vulnerable / scanned_hosts) * 100

#3. Kontrollera med en jämförelseoperator om andelen är större än 10.

if vulnerable_percentage > 10:
    result = "Andelen sårbara maskiner är större än 10%."


#4. Skriv ut resultatet.

print(result)