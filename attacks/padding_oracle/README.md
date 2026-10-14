# Padding Oracle Attack

## 1. Aim

To understand and demonstrate how a Padding Oracle Attack can recover
plaintext from an AES-CBC encrypted message without knowing the
encryption key.

## 2. Objectives

- Understand AES-CBC encryption.
- Understand PKCS#7 padding.
- Understand the role of a padding oracle.
- Implement a padding oracle attack.
- Recover plaintext bytes from right to left.
- Count the number of oracle queries.
- Understand how to prevent padding oracle vulnerabilities.

## 3. Theory

### AES-CBC

AES-CBC stands for Advanced Encryption Standard in Cipher Block Chaining
mode.

AES processes data in blocks of 16 bytes. In CBC mode, each plaintext
block is XORed with the previous ciphertext block before encryption.

The Initialization Vector (IV) is used for the first block.

During decryption:

P[i] = D(K, C[i]) XOR C[i-1]

Here:
- P[i] is the plaintext block.
- C[i] is the ciphertext block.
- D(K, C[i]) is the AES decryption operation.
- XOR is the exclusive OR operation.
- C[i-1] is the previous ciphertext block or the IV.

### PKCS#7 Padding

AES requires data to be processed in complete 16-byte blocks.

PKCS#7 padding adds bytes to make the plaintext length a multiple of
the block size.

Each padding byte contains the number of padding bytes added.

For example, if three padding bytes are required, they are:

03 03 03

### Padding Oracle

A padding oracle is a function that indicates whether decrypted data
has valid PKCS#7 padding.

It returns True for valid padding and False for invalid padding.

By modifying ciphertext blocks and observing the oracle's responses,
an attacker may recover plaintext without knowing the AES key.

## 4. Implementation

The experiment uses AES-CBC encryption and a padding-oracle function.

The attack modifies the previous ciphertext block and queries the
oracle to recover plaintext bytes, starting from the rightmost byte.

The attack implementation must not access or use the AES key.

## 5. Analysis

### Why does modifying the previous ciphertext block work?

CBC decryption is given by:

P[i] = D(K, C[i]) XOR C[i-1]

Changing C[i-1] changes P[i], even though C[i] remains unchanged.

An attacker uses this property to influence the decrypted bytes and
observe whether the resulting padding is valid.

### Oracle Queries

The implementation records the total number of padding-oracle queries.

The number of queries depends on the ciphertext, the attack algorithm,
and how the implementation handles ambiguous padding responses.

The actual query count must be recorded when the program runs.

## 6. Security Recommendations

- Prefer authenticated encryption such as AES-GCM or ChaCha20-Poly1305.
- Verify authentication before processing decrypted data.
- Avoid revealing whether a padding check specifically failed.
- Avoid leaking distinguishable timing or error responses.
- Use established and reviewed cryptographic libraries.

## 7. Conclusion

The Padding Oracle Attack demonstrates that revealing padding
validity can expose plaintext even when the encryption key is unknown.

Secure systems should use authenticated encryption and avoid exposing
information that allows attackers to distinguish padding failures.