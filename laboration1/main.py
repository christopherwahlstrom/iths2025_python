import requests
import sys


BASE_URL = "http://10.3.10.104:3000"

def get_token():
    """
    Steg 1: Hämta en token från API:et.
    Endpoint: POST /api/token
    """
    url = f"{BASE_URL}/api/token"
    print(f"[*] Requesting token from {url}...")
    
    try:
        response = requests.post(url)
        response.raise_for_status() 
        
        data = response.json()
        print(f"[+] Token acquired successfully!")
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"[-] Error getting an token: {e}")
        sys.exit(1)

def verify_token(token):
    """
    Steg 2: Verifiera token för att få en secret.
    Endpoint: POST /api/verify
    Header: Authorization: Bearer <token>
    """
    url = f"{BASE_URL}/api/verify"
    headers = {"Authorization": f"Bearer {token}"}
    print(f"[*] Verifying token at {url}...")

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        print(f"[+] Token verified! Secret received.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"[-] Error verifying token: {e}")
        if hasattr(e, 'response') and e.response is not None:
             print(f"Server response: {e.response.text}")
        sys.exit(1)

def get_flag(token, secret):
    """
    Steg 3: Hämta flaggan med token och secret.
    Endpoint: POST /api/flag
    Header: Authorization: Bearer <token>
    Body: {"secret": "<secret>"}
    """
    url = f"{BASE_URL}/api/flag"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"secret": secret}
    print(f"[*] Requesting flag from {url}...")

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        data = response.json()
        print(f" Flag acquired successfully!")
        return data
    except requests.exceptions.RequestException as e:
        print(f" Error getting flag: {e}")
        if hasattr(e, 'response') and e.response is not None:
             print(f"Server response: {e.response.text}")
        sys.exit(1)

def main():
    print("Starting an API solver...")
    
    token_data = get_token()
    token = token_data.get("token")
    
    if not token:
        print(" No token found in response")
        sys.exit(1)

    verification_data = verify_token(token)
    secret = verification_data.get("secret")
    
    if not secret:
        print(" No secret found in verification response")
        sys.exit(1)

    flag_data = get_flag(token, secret)
    print(f"\n Here is the flag:\n{flag_data.get('flag')}")

if __name__ == "__main__":
    main()
