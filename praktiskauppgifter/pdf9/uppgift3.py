import hashlib
import os

HASH_FILE = "hashes.txt"

def calculate_sha256(filepath):
    """Beräknar SHA-256 hash för en fil."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # Läs filen i block för att inte fylla minnet
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def scan_directory(directory="."):
    """Skannar mappen och returnerar en dictionary {filnamn: hash}."""
    files_hash = {}
    # Lista alla filer i nuvarande mapp (exkludera scriptet själv och hash-filen)
    for filename in os.listdir(directory):
        if os.path.isfile(filename) and filename not in [os.path.basename(__file__), HASH_FILE]:
            file_hash = calculate_sha256(filename)
            if file_hash:
                files_hash[filename] = file_hash
    return files_hash

def save_hashes(hashes):
    """Sparar hash-värden till fil."""
    with open(HASH_FILE, "w") as f:
        for filename, h in hashes.items():
            f.write(f"{filename}:{h}\n")
    print(f"Sparade {len(hashes)} hash-värden till {HASH_FILE}.")

def load_hashes():
    """Laddar hash-värden från fil."""
    hashes = {}
    if not os.path.exists(HASH_FILE):
        return {}
    
    with open(HASH_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(":")
            if len(parts) == 2:
                hashes[parts[0]] = parts[1]
    return hashes

def main():
    print("--- Filintegritetskontroll ---")
    
    if not os.path.exists(HASH_FILE):
        print(f"Ingen {HASH_FILE} hittades. Skapar en baslinje...")
        current_hashes = scan_directory()
        save_hashes(current_hashes)
    else:
        print(f"Jämför med sparade värden i {HASH_FILE}...")
        old_hashes = load_hashes()
        current_hashes = scan_directory()
        
        # Kolla efter ändringar
        all_files = set(old_hashes.keys()) | set(current_hashes.keys())
        
        modified = False
        for filename in all_files:
            old = old_hashes.get(filename)
            new = current_hashes.get(filename)
            
            if old and new and old != new:
                print(f"[VARNING] Filen '{filename}' har MODIFIERATS!")
                modified = True
            elif old and not new:
                print(f"[INFO] Filen '{filename}' har tagits bort.")
                modified = True
            elif not old and new:
                print(f"[INFO] Ny fil upptäckt: '{filename}'")
                modified = True
        
        if not modified:
            print("Inga ändringar upptäckta. Allt ser bra ut.")
        else:
            # Uppdatera hash-filen?
            val = input("\nVill du uppdatera hash-filen med de nya värdena? (j/n): ")
            if val.lower() == "j":
                save_hashes(current_hashes)

if __name__ == "__main__":
    main()
