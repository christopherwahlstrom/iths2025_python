# Bygg ett verktyg som löser ett flerstegs-API   


## Målet med laborationen
I denna uppgift ska ni bygga ett Python-skript som kommunicerar med ett API på tailscale nätet.  

Vi lär oss:

- Göra **flera requests i rad**
- Skicka **parametrar** till ett API
- Ta emot och förstå **JSON-svar**
- Hantera **fel** med `try/except`
- Använda **funktioner** för struktur och tydlighet
- Lösa ett problem som ***inte går att göra manuellt**

---
## Instruktioner

Läs swagger dokumentationen på http://10.3.10.104:3000/docs
Bygga ett Python-skript som kommunicerar med ett API på tailscale nätet och får ut flaggan
API -> http://10.3.10.104:3000

---

## Inlämning

Ladda upp ert script med tillhörande requirements.txt på github och lämna in länken på itslearning.
Repo struktur:

```
<namn>.py
requirements.py§
```

Readme -> Valfritt

Det ska vara möjligt att clona ner repot och köra pip install -r requirement.txt (i en venv) och sedan köra scriptet och få ut flaggan

---

##  Varför går det inte att göra manuellt?

API:t har begränsningar som:

- Token gäller endast mycket kort tid
- Sekvensen måste vara rätt
- Svar från ett steg behövs direkt i nästa

Därför måste ni skriva kod som:

1. Hämtar data  
2. Tolkar den  
3. Skickar vidare till nästa steg  


---

#  Slutmålet

När hela kedjan är rätt byggd får ni en **flagga** i stil med:

```
FLAG{xxxxx}

Svaret är : FLAG{automation_beats_manual}

```

Flaggan visar att ni lyckats bygga ett automatiserat verktyg som löser hela API-flödet.

---
