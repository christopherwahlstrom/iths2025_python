import argparse
import os
from cryptography.fernet import Fernet

def load_key(keyfile):
    """Laddar nyckeln från angiven fil."""
    try:
        return open(keyfile, "rb").read()
    except FileNotFoundError:
        print(f"Fel: Nyckelfilen '{keyfile}' hittades inte.")
        exit(1)

def encrypt(args):
    key = load_key(args.key)
    f = Fernet(key)
    
    try:
        with open(args.file, "rb") as file:
            file_data = file.read()
            
        encrypted_data = f.encrypt(file_data)
        
        output_file = args.file + ".enc"
        with open(output_file, "wb") as file:
            file.write(encrypted_data)
            
        print(f"Krypterade '{args.file}' -> '{output_file}'")
    except FileNotFoundError:
        print(f"Fel: Filen '{args.file}' hittades inte.")

def decrypt(args):
    key = load_key(args.key)
    f = Fernet(key)
    
    try:
        with open(args.file, "rb") as file:
            encrypted_data = file.read()
            
        decrypted_data = f.decrypt(encrypted_data)
        
        # Om filen heter fil.txt.enc -> fil.txt
        output_file = args.file.replace(".enc", "")
        # Fallback om den inte hette .enc
        if output_file == args.file:
            output_file = "decrypted_" + args.file
            
        with open(output_file, "wb") as file:
            file.write(decrypted_data)
            
        print(f"Dekrypterade '{args.file}' -> '{output_file}'")
    except Exception as e:
        print(f"Fel vid dekryptering: {e}")

def main():
    parser = argparse.ArgumentParser(description="Ett CLI-verktyg för filkryptering.")
    subparsers = parser.add_subparsers(dest="command", help="Kommando att köra")

    # Encrypt kommando
    encrypt_parser = subparsers.add_parser("encrypt", help="Kryptera en fil")
    encrypt_parser.add_argument("key", help="Sökväg till nyckelfilen")
    encrypt_parser.add_argument("file", help="Filen som ska krypteras")
    encrypt_parser.set_defaults(func=encrypt)

    # Decrypt kommando
    decrypt_parser = subparsers.add_parser("decrypt", help="Dekryptera en fil")
    decrypt_parser.add_argument("key", help="Sökväg till nyckelfilen")
    decrypt_parser.add_argument("file", help="Filen som ska dekrypteras")
    decrypt_parser.set_defaults(func=decrypt)

    args = parser.parse_args()

    if args.command:
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
