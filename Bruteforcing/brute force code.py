from zipfile import ZipFile, BadZipFile
import sys

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except (RuntimeError, BadZipFile, ValueError):
        return False

def main():
    print("[+] Beginning bruteforce")

    try:
        with ZipFile('enc.zip') as zf:
            with open('rockyou.ini', 'rb') as f:  # Typically 'rockyou.txt'
                for line in f:
                    password = line.strip()
                    if attempt_extract(zf, password):
                        print(f"[+] Password found: {password.decode('utf-8')}")
                        return
                    else:
                        print(f"[-] Incorrect password: {password.decode('utf-8', errors='ignore')}")
    except FileNotFoundError as e:
        print(f"[!] File not found: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        sys.exit(1)

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
