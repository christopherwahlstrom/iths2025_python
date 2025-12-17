import argparse

parser = argparse.ArgumentParser(description="Simple hash cracker")

parser.add_argument("wordlist")

parser.add_argument("-v", "--verbose", action="store_true")

parser.add_argument("--algorithm", default="sha256")

parser.add_argument("--algorithm", choices=["md5", "sha1", "sha256"])

parser.add_argument("-p", type=int)

parser.add_argument("targets", nargs="+")

parser.add_argument_group("Authentication")

parser.add_subparsers(dest="command")

args = parser.parse_args()

args.wordlist

