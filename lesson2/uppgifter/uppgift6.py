#Praktiskt uppgift 06
#Analysera en sträng från en fiktiv loggfil.


#1. Skapa variabeln: log = "2025-11-13 12:55:21 - LOGIN FAILED - user=root"

log = "2025-11-13 12:55:21 - LOGIN FAILED - user=root"

#2. Extrahera datum, status och användarnamn med slicing.

extracted_date = log[0:10]
extracted_status = log[22:34]
extracted_user = log[41:45]

#3. Skriv ut varje del på en ny rad.

print("Datum:", extracted_date)
print("Status:", extracted_status)
print("Användare:", extracted_user)


#4. Vänd sedan hela strängen baklänges.
reversed_log = log[::-1]
print("Omvänd logg:", reversed_log)

