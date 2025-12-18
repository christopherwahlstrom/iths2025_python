"""
Uppgift 2: HTML Image Replacer

Instruktioner:
1. Skriv ett Python-skript som går igenom alla .html-filer i en katalog (t.ex. nuvarande mapp).
2. Använd regex för att hitta och ersätta alla <img>-taggar med en placeholder: <img src="placeholder.jpg">.
3. Spara filen med ändringarna.

Tips:
- Använd `os` eller `pathlib` för att hitta filer.
- Använd `re.sub()` för att ersätta text.
- Regex för img-tagg kan vara lite klurigt, men börja enkelt. T.ex. r'<img[^>]+>'
"""

import os
import re

current_dir = os.getcwd()
print(f"Letar efter HTML-filer i: {current_dir}")

# Regex-mönster för att hitta img-taggar
# Förklaring: <img följt av vad som helst fram till >
img_pattern = r'<img[^>]+>'
placeholder = '<img src="placeholder.jpg">'

for filename in os.listdir(current_dir):
    if filename.endswith(".html"):
        print(f"Bearbetar {filename}...")
        
        # 1. Läs filen
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 2. Hitta och ersätt (re.sub returnerar den nya texten)
        new_content = re.sub(img_pattern, placeholder, content)
        
        # 3. Kolla om något ändrades (bara för att vara tydlig)
        if content != new_content:
            print(f"  -> Ersatte bilder i {filename}")
            
            # 4. Spara ändringarna (skriv över filen)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(new_content)
        else:
            print(f"  -> Inga bilder hittades i {filename}")

print("Klart!")