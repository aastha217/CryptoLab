from shift_cipher import decrypt


# Expected frequency of each letter in English
english_frequency = {
    'a': 0.0812,
    'b': 0.0149,
    'c': 0.0271,
    'd': 0.0432,
    'e': 0.1202,
    'f': 0.0230,
    'g': 0.0203,
    'h': 0.0592,
    'i': 0.0731,
    'j': 0.0010,
    'k': 0.0069,
    'l': 0.0398,
    'm': 0.0261,
    'n': 0.0695,
    'o': 0.0768,
    'p': 0.0182,
    'q': 0.0011,
    'r': 0.0602,
    's': 0.0628,
    't': 0.0910,
    'u': 0.0288,
    'v': 0.0111,
    'w': 0.0209,
    'x': 0.0017,
    'y': 0.0211,
    'z': 0.0007
}


def chi_square_score(text):
    letters = []

    for ch in text.lower():
        if ch.isalpha():
            letters.append(ch)

    total = len(letters)

    if total == 0:
        return float("inf")

    observed = {}

    for letter in english_frequency:
        observed[letter] = 0

    for ch in letters:
        observed[ch] += 1

    score = 0

    for letter in english_frequency:
        expected = english_frequency[letter] * total

        if expected > 0:
            score += ((observed[letter] - expected) ** 2) / expected

    return score


def find_key(ciphertext):
    best_key = 0
    best_score = float("inf")
    best_text = ""

    for key in range(26):
        decrypted_text = decrypt(ciphertext, key)
        score = chi_square_score(decrypted_text)

        print("Key:", key, "| Chi-Square:", score,
              "| Text:", decrypted_text)

        if score < best_score:
            best_score = score
            best_key = key
            best_text = decrypted_text

    return best_key, best_score, best_text


if __name__ == "__main__":
    ciphertext = "KHOOR ZRUOG"

    key, score, plaintext = find_key(ciphertext)

    print("\nPredicted Key:", key)
    print("Chi-Square Score:", score)
    print("Plaintext:", plaintext)