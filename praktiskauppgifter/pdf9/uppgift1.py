import os
from cryptography.fernet import Fernet

# Filnamn för att spara nyckeln
KEY_FILE = "secret.key"

def generate_key():
    """Genererar en nyckel och sparar den i en fil."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        print(f"Nyckel genererad och sparad som {KEY_FILE}")
    else:
        print(f"Nyckel finns redan ({KEY_FILE}). Använder den.")

def load_key():
    """Laddar nyckeln från filen."""
    return open(KEY_FILE, "rb").read()

def encrypt_file(filename):
    """Krypterar filen, sparar som .enc och tar bort originalet."""
    key = load_key()
    f = Fernet(key)

    try:
        with open(filename, "rb") as file:
            file_data = file.read()
        
        encrypted_data = f.encrypt(file_data)
        
        enc_filename = filename + ".enc"
        with open(enc_filename, "wb") as file:
            file.write(encrypted_data)
            
        os.remove(filename) # Tar bort originalet enligt uppgiften
        print(f"Filen '{filename}' har krypterats till '{enc_filename}' och originalet är borttaget.")
        
    except FileNotFoundError:
        print(f"Kunde inte hitta filen: {filename}")

def decrypt_file(enc_filename):
    """Dekrypterar .enc-filen och återskapar originalet."""
    key = load_key()
    f = Fernet(key)

    try:
        with open(enc_filename, "rb") as file:
            encrypted_data = file.read()
        
        decrypted_data = f.decrypt(encrypted_data)
        
        # Ta bort .enc ändelsen för att få originalnamnet
        original_filename = enc_filename.replace(".enc", "")
        
        with open(original_filename, "wb") as file:
            file.write(decrypted_data)
            
        os.remove(enc_filename) # Tar bort den krypterade filen
        print(f"Filen '{enc_filename}' har dekrypterats till '{original_filename}'.")
        
    except Exception as e:
        print(f"Ett fel uppstod vid dekryptering (fel nyckel?): {e}")

def main():
    print("--- Enkel Filkrypterare ---")
    generate_key() # Se till att vi har en nyckel
    
    while True:
        print("\n1. Kryptera fil")
        print("2. Dekryptera fil")
        print("3. Avsluta")
        val = input("Val: ")
        
        if val == "1":
            fil = input("Ange filnamn att kryptera: ")
            encrypt_file(fil)
        elif val == "2":
            fil = input("Ange filnamn att dekryptera (slutar på .enc): ")
            decrypt_file(fil)
        elif val == "3":
            break
        else:
            print("Ogiltigt val.")

if __name__ == "__main__":
    main()
