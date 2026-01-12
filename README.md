# Programmering för Penetrationstestare (Kurs 4)

Detta repository innehåller kod, laborationer och anteckningar för kursen **Programmering för penetrationstestare**. Syftet med kursen är att lära sig utveckla egna säkerhetsverktyg, automatisera attacker och förstå hur man interagerar med system på djupet med Python och C.

## 🛠 Miljö & Moderna Verktyg
Kursen lägger stor vikt vid att använda moderna, snabba verktyg för pakethantering och isolerade miljöer för att undvika konflikter och "dependency hell".

* **Språk:** Python 3, C (GCC/MinGW), C# (.NET)
* **Pakethantering:** `uv` (Rust-baserad, ersätter pip), `pipx`
* **Editor:** Visual Studio Code

### Setup (Best Practice)
Vi använder `uv` för blixtsnabba virtuella miljöer.

```bash
# 1. Installera verktyg globalt men isolerat
pipx install uv
pipx install httpie

# 2. Initiera projektmiljö med uv
uv venv

# 3. Aktivera miljön
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 4. Installera beroenden
uv pip install requests paramiko cryptography shodan beautifulsoup4 selenium scapy



Nätverk & Sockets
Att bygga egna nätverksverktyg från grunden.

Sockets: Skapa egna klienter/servrar (TCP/UDP) och chattprogram.

Scapy: Manipulering och analys av nätverkspaket på låg nivå.

DNS: Skript för DNS-lookups och Reverse DNS.

🔹 SSH & Brute-force (Paramiko)
Automatisering av attacker mot infrastruktur.

Paramiko: Skapa SSH-klienter för att fjärrstyra servrar.

Brute-force: Skript som testar användarnamn/lösenord mot SSH-tjänster.

Exfiltration: Hämta känsliga filer (t.ex. /etc/passwd) automatiskt vid lyckat intrång.

🔹 Web Scraping & API:er
Att extrahera data från webben och interagera med tjänster.

Web Scraping: BeautifulSoup och Selenium för att hämta data från statiska och dynamiska sidor (JS).

API-anrop: Konsumera REST-API:er (JSON) med requests.

Shodan: Använda Shodans API för att scanna internet efter sårbara enheter.

🔹 Kryptering & Obfuskering
Säkerhet kring data och loggar.

Hashing: MD5, SHA-256 och saltning av lösenord.

Kryptering: Symmetrisk (Fernet) och Asymmetrisk (RSA) kryptering med cryptography-biblioteket.

Regex: Mönstermatchning för att hitta e-postadresser och känslig data i loggar.

🔹 Kompilering & Low-level
Förståelse för kompilerade språk i pentest-sammanhang.

C & Makefiles: Kompilering av exploits med gcc och make.

Cross-compilation: Bygga Windows-binärer (.exe) från Linux med MinGW.

C# / .NET: Bygga tools med csc och dotnet build.

📂 Projekt: Shellcode XOR Encryptor
Ett slutprojekt där vi bygger ett CLI-verktyg för att obfuskera shellcode. Målet är att skapa en payload som kan kringgå enklare signaturbaserade detektioner.

Funktionalitet:

Läser in binär shellcode från fil.

Krypterar payloaden med en XOR-nyckel.

Genererar output i C-format (array) redo att klistras in i en loader.