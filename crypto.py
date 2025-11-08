from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Kunci berhasil dibuat: key.key")

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"[+] File '{filename}' berhasil dienkripsi.")

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filename, "wb") as dec_file:
        dec_file.write(decrypted)

    print(f"[+] File '{filename}' berhasil didekripsi.")

if __name__ == "__main__":
    print("=== KRIPTOGRAFI FILE (TEXT, JPG, PDF) ===")
    print("1. Generate Key")
    print("2. Encrypt File (timpa file asli)")
    print("3. Decrypt File (kembalikan file asli)")

    choice = input("Pilih (1/2/3): ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        file_name = input("Masukkan nama file yang akan dienkripsi: ")
        if os.path.exists(file_name):
            encrypt_file(file_name)
        else:
            print("[!] File tidak ditemukan.")

    elif choice == "3":
        file_name = input("Masukkan nama file yang akan didekripsi: ")
        if os.path.exists(file_name):
            decrypt_file(file_name)
        else:
            print("[!] File tidak ditemukan.")

    else:
        print("Pilihan tidak valid.")

