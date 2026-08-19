import os

from shift_cipher import encrypt, decrypt
from brute_force_dictionary import load_dictionary, brute_force
from chi_square_attack import find_key as chi_square_find_key


def main():
    while True:
        print("\n===== Shift Cipher Cryptanalysis =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Dictionary Attack")
        print("4. Chi-Square Attack")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter plaintext: ")
            key = int(input("Enter key (0-25): "))

            ciphertext = encrypt(text, key)

            print("Encrypted text:", ciphertext)

        elif choice == "2":
            text = input("Enter ciphertext: ")
            key = int(input("Enter key (0-25): "))

            plaintext = decrypt(text, key)

            print("Decrypted text:", plaintext)

        elif choice == "3":
            ciphertext = input("Enter ciphertext: ")

            script_dir = os.path.dirname(os.path.abspath(__file__))

            dict_path = os.path.join(
                script_dir,
                "..",
                "dictionary",
                "english_words.txt"
            )

            dictionary = load_dictionary(dict_path)

            results = brute_force(ciphertext, dictionary)

            score, key, plaintext = results[0]

            print("\nBest Dictionary Result:")
            print("Predicted Key:", key)
            print("Dictionary Score:", score)
            print("Predicted Plaintext:", plaintext)

        elif choice == "4":
            ciphertext = input("Enter ciphertext: ")

            key, score, plaintext = chi_square_find_key(ciphertext)

            print("\nBest Chi-Square Result:")
            print("Predicted Key:", key)
            print("Chi-Square Score:", score)
            print("Predicted Plaintext:", plaintext)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()