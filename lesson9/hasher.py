import argparse
import hashlib

parser = argparse.ArgumentParser(description="My hashtool")
sub = parser.add_subparsers(dest="cmd")

crack = sub.add_parser("crack", help="Crack a hash")
crack.add_argument("hash", help="Hash value to be cracked")

crack.add_argument("wordlist", help="Path to wordlist(one line per password)")

crack.add_argument("-a", "--algorithm", choices=["md5", "sha1", "sha256"], default="sha256", help="Algorithm (default sha256)")

crack.add_argument("-v", "--verbose", action="store_true" ,help="Debug")

identify = sub.add_parser("identify", help="Identify hashes")

identify.add_argument("hash")

args = parser.parse_args()

if args.cmd == "identify":
    pass


# if args.algorithm == "md5":
#     hash_func = hashlib.md5
# if args.algorithm == "sha1":
#     hash_func = hashlib.sha1
# if args.algorithm == "sha256":
#     hash_func = hashlib.sha256

if args.cmd == "crack":
    hash_func = getattr(hashlib, args.algorithm)

    with open(args.wordlist, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            password = line.strip()
            digest = hash_func(password.encode()).hexdigest()

            if args.verbose:
                print(f"[*] Trying: {password}")
            
            if digest == args.hash:
                print(f"[+] Password found {password}")
                break
        else:
            print("[-] Password not found in wordlist")
