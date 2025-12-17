#Skapa ett script som konsumerar Sveriges Radios API på valfritt sett. 

#Använd gärna moduler för att dela upp scriptet i flera filer.

#API dokumentation för Sveriges radios api: https://api.sr.se/api/documentation/v2/index.html

# Hämta data från Sveriges Radios API och skriv ut titlarna på de senaste nyheterna.


import requests 

def get_channels():
     url = "http://api.sr.se/api/v2/channels?format=json&pagination=false"

     try:
          response = requests.get(url)

          if response.status_code == 200:
               data = response.json()

               return data ['channels']
          else:
               print(f"Fel vid hämtning av data: {response.status_code}")
               return []
     
     except requests.exceptions.RequestException as e:
          print(f"Ett fel uppstod: {e}")
          return []
     
     
