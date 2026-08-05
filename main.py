import os
from datetime import datetime

LOG_FILE = "execution.log"

def write_log(choice):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - Selected Option: {choice}\n")


def file_analysis():
    filename = input("Enter filename from datasets folder: ")

    path = os.path.join("datasets", filename)

    if not os.path.exists(path):
        print("File not found.")
        return

    with open(path, "r") as f:
        text = f.read()

    chars = len(text)
    words = len(text.split())
    lines = len(text.splitlines())

    freq = {}

    for ch in text.lower():
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1

    print("\nFile Analysis")
    print("Characters:", chars)
    print("Words:", words)
    print("Lines:", lines)
    print("Letter Frequency:")

    for k in sorted(freq):
        print(k, ":", freq[k])


while True:
    print("\n===== CryptoLabX =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze Text File")
    print("5. Exit")

    ch = input("Enter choice: ")

    write_log(ch)

    if ch == "1":
        print("Coming Soon!")

    elif ch == "2":
        print("Coming Soon!")

    elif ch == "3":
        print("Coming Soon!")

    elif ch == "4":
        file_analysis()

    elif ch == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")