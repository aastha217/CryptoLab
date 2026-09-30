from collections import Counter


def generate_key_matrix(keyword):
    keyword = keyword.upper()
    keyword = keyword.replace("J", "I")

    key = ""

    # Add keyword letters without repetition
    for ch in keyword:
        if ch.isalpha() and ch not in key:
            key += ch

    # Add remaining alphabet
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in key:
            key += ch

    matrix = []

    for i in range(0, 25, 5):
        matrix.append(key[i:i + 5])

    return matrix


def prepare_plaintext(plaintext):
    plaintext = plaintext.upper()

    result = ""

    for ch in plaintext:
        if ch.isalpha():
            if ch == "J":
                ch = "I"

            result += ch

    return result


def create_digraphs(plaintext):
    digraphs = []

    i = 0

    while i < len(plaintext):

        first = plaintext[i]

        # If only one character is left
        if i + 1 >= len(plaintext):
            digraphs.append(first + "X")
            i += 1

        else:
            second = plaintext[i + 1]

            # Repeated letters
            if first == second:
                digraphs.append(first + "X")
                i += 1

            else:
                digraphs.append(first + second)
                i += 2

    return digraphs


def find_position(matrix, letter):

    for row in range(5):
        for col in range(5):

            if matrix[row][col] == letter:
                return row, col

    return -1, -1


def playfair_encrypt(digraphs, matrix):

    ciphertext = ""

    for pair in digraphs:

        first = pair[0]
        second = pair[1]

        row1, col1 = find_position(matrix, first)
        row2, col2 = find_position(matrix, second)

        # Same row
        if row1 == row2:

            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]

        # Same column
        elif col1 == col2:

            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]

        # Rectangle rule
        else:

            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext


def playfair_decrypt(ciphertext, matrix):

    plaintext = ""

    for i in range(0, len(ciphertext), 2):

        first = ciphertext[i]
        second = ciphertext[i + 1]

        row1, col1 = find_position(matrix, first)
        row2, col2 = find_position(matrix, second)

        # Same row
        if row1 == row2:

            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]

        # Same column
        elif col1 == col2:

            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]

        # Rectangle rule
        else:

            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext


def digraph_frequency(ciphertext):

    frequency = Counter()

    for i in range(0, len(ciphertext), 2):

        digraph = ciphertext[i:i + 2]
        frequency[digraph] += 1

    return frequency


def verify(plaintext, decrypted_text):

    prepared = prepare_plaintext(plaintext)
    digraphs = create_digraphs(prepared)

    expected = ""

    for pair in digraphs:
        expected += pair

    if expected == decrypted_text:
        return "SUCCESS"

    return "FAILED"


def main():

    keyword = "MONARCHY"
    plaintext = "INSTRUMENTS"

    # Generate key matrix
    matrix = generate_key_matrix(keyword)

    print("Key Matrix")

    for row in matrix:
        print(" ".join(row))

    # Prepare plaintext
    prepared_text = prepare_plaintext(plaintext)

    # Create digraphs
    digraphs = create_digraphs(prepared_text)

    print("\nPrepared Digraphs:")
    print(" ".join(digraphs))

    # Encryption
    ciphertext = playfair_encrypt(digraphs, matrix)

    print("\nCiphertext:")
    print(ciphertext)

    # Decryption
    decrypted_text = playfair_decrypt(ciphertext, matrix)

    print("\nDecrypted Text:")
    print(decrypted_text)

    # Frequency analysis
    frequency = digraph_frequency(ciphertext)

    print("\nDigraph Frequency:")

    for digraph, count in frequency.items():
        print(digraph, ":", count)

    # Verification
    result = verify(plaintext, decrypted_text)

    print("\nVerification:")
    print(result)


if __name__ == "__main__":
    main()