
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 16


def encrypt_message(plaintext):
    # Generate a random secret key and IV.
    key = get_random_bytes(BLOCK_SIZE)
    iv = get_random_bytes(BLOCK_SIZE)

    # Encrypt using AES-CBC with PKCS#7 padding.
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))

    # The attacker can call this function but cannot access key.
    def padding_oracle(test_iv, test_ciphertext):
        try:
            if len(test_iv) != BLOCK_SIZE:
                return False

            if (
                len(test_ciphertext) == 0
                or len(test_ciphertext) % BLOCK_SIZE != 0
            ):
                return False

            cipher = AES.new(key, AES.MODE_CBC, test_iv)
            decrypted = cipher.decrypt(test_ciphertext)

            # Returns True only if PKCS#7 padding is valid.
            unpad(decrypted, BLOCK_SIZE)
            return True

        except (ValueError, TypeError):
            return False

    return iv, ciphertext, padding_oracle


if __name__ == "__main__":
    message = b"Padding oracle lab demonstration"

    iv, ciphertext, oracle = encrypt_message(message)

    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())
    print("Original padding valid:", oracle(iv, ciphertext))
