#Extra uppgift
#Kräver koncept vi inte gått igenom ännu
#Skapa ett kort Python-program som kontrollerar om
#ett inloggningsförsök ska tillåtas eller blockeras baserat på flera villkor:
# - username får inte vara tomt.
# - password får inte vara kortare än 8 tecken.
#- login_attempts får inte överstiga 5.

username = "admin"
password = "securePass123"
login_attempts = 4

if not username:
    print("Inloggning blockerad: Användarnamn får inte vara tomt.")
elif len(password) < 8:
    print("Inloggning blockerad: Lösenordet är för kort.")
elif login_attempts > 5:
    print("Inloggning blockerad: För många inloggningsförsök.")
else:
    print("Inloggning tillåten.")

    