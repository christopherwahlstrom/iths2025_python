# pylint: disable=missing-module-docstring

#Ladda ner log.txt från itslearning och lägg filen i samma katalog som ditt skript.. 
# 
# Lägg denna fil i samma katalog som ditt python-skript.

#Öppna filen och läs in den

#Skriv ut varje rad i filen som innehåller "Failed login attempt" (utan tomrader)

with open("log.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "Failed login attempt" in line:
            print(line.strip())



