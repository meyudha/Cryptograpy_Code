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

    with open(filename + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"[+] File '{filename}' berhasil dienkripsi -> {filename}.encrypted")

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)
    original_name = filename.replace(".encrypted", "")

    with open(original_name, "wb") as dec_file:
        dec_file.write(decrypted)

    print(f"[+] File '{filename}' berhasil didekripsi -> {original_name}")

if __name__ == "__main__":
    print("=== KRIPTOGRAFI FILE (TEXT, JPG, PDF) ===")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")

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
        file_name = input("Masukkan nama file terenkripsi (.encrypted): ")
        if os.path.exists(file_name):
            decrypt_file(file_name)
        else:
            print("[!] File tidak ditemukan.")

    else:
        print("Pilihan tidak valid.")
