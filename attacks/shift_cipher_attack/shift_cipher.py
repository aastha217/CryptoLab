def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += ch

    return result


def decrypt(text, key):
    return encrypt(text, -key)


# Testing
plaintext = "HELLO WORLD"
key = 3

ciphertext = encrypt(plaintext, key)
print("Plaintext :", plaintext)
print("Key       :", key)
print("Encrypted :", ciphertext)

decrypted = decrypt(ciphertext, key)
print("Decrypted :", decrypted)