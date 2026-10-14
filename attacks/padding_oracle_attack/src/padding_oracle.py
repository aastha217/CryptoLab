
from aes_cbc_oracle import encrypt_message

BLOCK_SIZE = 16


def padding_oracle_attack(iv, ciphertext, oracle):
    query_count = 0

    def query(test_iv, test_ciphertext):
        nonlocal query_count
        query_count += 1
        return oracle(test_iv, test_ciphertext)

    if len(iv) != BLOCK_SIZE:
        raise ValueError("Invalid IV length")

    if not ciphertext or len(ciphertext) % BLOCK_SIZE != 0:
        raise ValueError("Invalid ciphertext length")

    blocks = [
        ciphertext[i:i + BLOCK_SIZE]
        for i in range(0, len(ciphertext), BLOCK_SIZE)
    ]

    recovered_plaintext = bytearray()

    for block_index in range(len(blocks)):
        target = blocks[block_index]

        if block_index == 0:
            previous = iv
        else:
            previous = blocks[block_index - 1]

        intermediate = [0] * BLOCK_SIZE
        crafted = bytearray(BLOCK_SIZE)

        print("Attacking block", block_index + 1)

        # Recover bytes from right to left.
        for padding_value in range(1, BLOCK_SIZE + 1):
            position = BLOCK_SIZE - padding_value

            # Force known suffix bytes to match the new padding.
            for j in range(position + 1, BLOCK_SIZE):
                crafted[j] = intermediate[j] ^ padding_value

            found = False

            for guess in range(256):
                crafted[position] = guess

                # Treat crafted preceding block as the IV.
                valid = query(bytes(crafted), target)

                if not valid:
                    continue

                # Reject accidental longer valid padding.
                if padding_value == 1:
                    crafted[position - 1] ^= 1

                    confirmed = query(bytes(crafted), target)

                    crafted[position - 1] ^= 1

                    if not confirmed:
                        continue

                # D_K(C_i)[position]
                intermediate[position] = guess ^ padding_value
                found = True
                break

            if not found:
                raise RuntimeError(
                    "Failed at block {}, byte {}".format(
                        block_index + 1, position
                    )
                )

        # Recover plaintext by XORing with the ORIGINAL
        # previous ciphertext block (or original IV).
        plaintext_block = bytearray(BLOCK_SIZE)

        for j in range(BLOCK_SIZE):
            plaintext_block[j] = intermediate[j] ^ previous[j]

        recovered_plaintext.extend(plaintext_block)

        print("Block", block_index + 1, "recovered!")

    # Remove PKCS#7 padding.
    padding_length = recovered_plaintext[-1]

    if not 1 <= padding_length <= BLOCK_SIZE:
        raise ValueError("Invalid recovered padding length")

    expected = bytes([padding_length]) * padding_length

    if bytes(recovered_plaintext[-padding_length:]) != expected:
        raise ValueError("Invalid recovered PKCS#7 padding")

    plaintext = bytes(recovered_plaintext[:-padding_length])

    return plaintext, query_count


if __name__ == "__main__":
    original = b"Padding oracle lab demonstration"

    iv, ciphertext, oracle = encrypt_message(original)

    print("\n===== AES-CBC PADDING ORACLE ATTACK =====\n")

    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())
    print()

    recovered, queries = padding_oracle_attack(
        iv, ciphertext, oracle
    )

    print("\n========== RESULTS ==========")
    print("Original plaintext:", original.decode("utf-8"))
    print("Recovered plaintext:", recovered.decode("utf-8"))
    print("Total oracle queries:", queries)
    print("AES key accessed by attack: No")
    print("Recovery successful:", recovered == original)
    print("=============================")
