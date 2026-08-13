import hashlib
import os
from cryptography.fernet import Fernet


# =========================================================
# ENCRYPTION KEY
# =========================================================

KEY_FILE = "secret.key"


def generate_key():

    if not os.path.exists(KEY_FILE):

        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)

        print("Encryption key created successfully! 🔑")


def load_key():

    generate_key()

    with open(KEY_FILE, "rb") as file:
        return file.read()


# =========================================================
# FILE SHA-256 HASH
# =========================================================

def calculate_file_hash(file_path):
    """
    Calculate SHA-256 hash of an evidence file.
    """

    sha256 = hashlib.sha256()

    try:

        with open(file_path, "rb") as file:

            while True:

                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:

        print("File not found! ❌")

        return None


# =========================================================
# VERIFY FILE INTEGRITY
# =========================================================

def verify_file_integrity(file_path, original_hash):
    """
    Compare current file hash with original hash.
    """

    current_hash = calculate_file_hash(file_path)

    if current_hash is None:

        return False

    if current_hash == original_hash:

        print("Evidence Integrity Verified! ✅")

        return True

    else:

        print(
            "WARNING: Evidence File Has Been Modified! ❌"
        )

        return False


# =========================================================
# ENCRYPT FILE
# =========================================================

def encrypt_file(file_path):

    if not os.path.exists(file_path):

        print("File not found! ❌")

        return None

    key = load_key()

    cipher = Fernet(key)

    with open(file_path, "rb") as file:

        data = file.read()

    encrypted_data = cipher.encrypt(data)

    encrypted_path = file_path + ".encrypted"

    with open(encrypted_path, "wb") as file:

        file.write(encrypted_data)

    print("\nFile encrypted successfully! 🔒")
    print("Encrypted file:", encrypted_path)

    return encrypted_path


# =========================================================
# DECRYPT FILE
# =========================================================

def decrypt_file(encrypted_path):

    if not os.path.exists(encrypted_path):

        print("Encrypted file not found! ❌")

        return None

    key = load_key()

    cipher = Fernet(key)

    try:

        with open(encrypted_path, "rb") as file:

            encrypted_data = file.read()

        decrypted_data = cipher.decrypt(
            encrypted_data
        )

        if encrypted_path.endswith(".encrypted"):

            decrypted_path = encrypted_path[:-10]

        else:

            decrypted_path = (
                encrypted_path + ".decrypted"
            )

        with open(decrypted_path, "wb") as file:

            file.write(decrypted_data)

        print("\nFile decrypted successfully! 🔓")
        print("Decrypted file:", decrypted_path)

        return decrypted_path

    except Exception:

        print(
            "\nUnable to decrypt file! "
            "Invalid key or corrupted file. ❌"
        )

        return None


# =========================================================
# TEST SECURITY SYSTEM
# =========================================================

if __name__ == "__main__":

    print("========================================")
    print("       DIGITAL EVIDENCE SECURITY")
    print("========================================")

    file_path = input(
        "Enter evidence file path: "
    )

    if os.path.exists(file_path):

        file_hash = calculate_file_hash(
            file_path
        )

        print("\nSHA-256 Hash:")
        print(file_hash)

        print("\n1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            encrypt_file(file_path)

        elif choice == "2":

            decrypt_file(file_path)

        elif choice == "3":

            print(
                "\nSecurity system test completed! ✅"
            )

        else:

            print("\nInvalid choice! ❌")

    else:

        print("\nFile does not exist! ❌")