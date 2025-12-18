"""
Uppgift 1: Simulerad dataexfiltration

Instruktioner:
1. Skapa ett Python-skript som läser innehållet i en textfil som heter 'users.txt'.
2. Använd regex (modulen `re`) för att hitta alla e-postadresser i filen.
3. Skriv ut e-postadresserna i terminalen.
4. Spara alla hittade e-postadresser i en ny fil som heter 'emails.txt'.

Tips:
- Importera modulen `re`.
- Använd `re.findall()` för att hitta mönster.
- Ett enkelt regex för e-post kan se ut så här: r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
"""

import re

filename = "users.txt"

try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print("--- Filinnehåll ---")
        print(content)
        print("-------------------")

        # Regex för att hitta e-postadresser
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)

        print("Hittade e-postadresser:")
        for email in emails:
            print(email)

        # Spara e-postadresser i en ny fil
        with open('emails.txt', 'w', encoding="utf-8") as email_file:
            for email in emails:
                email_file.write(email + '\n')

        print(f"\nTotalt {len(emails)} e-postadresser sparade i 'emails.txt'.")

except FileNotFoundError:
    print(f"Kunde inte hitta filen {filename}")


