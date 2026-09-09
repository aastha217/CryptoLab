import re
from collections import Counter, defaultdict


# English letter frequencies
ENGLISH_FREQ = [
    0.082, 0.015, 0.028, 0.043, 0.127,
    0.022, 0.020, 0.061, 0.070, 0.0015,
    0.0077, 0.040, 0.024, 0.067, 0.075,
    0.019, 0.00095, 0.060, 0.063, 0.091,
    0.028, 0.0098, 0.024, 0.0015, 0.020,
    0.00074
]


def clean_ciphertext(ciphertext):
    """Remove spaces/special characters and convert to uppercase."""
    return re.sub(r'[^A-Z]', '', ciphertext.upper())


def find_repeated_patterns(ciphertext, min_length=3, max_length=5):
    """Find repeated 3-5 letter sequences and their positions."""
    patterns = defaultdict(list)

    for length in range(min_length, max_length + 1):
        for i in range(len(ciphertext) - length + 1):
            pattern = ciphertext[i:i + length]
            patterns[pattern].append(i)

    return {
        pattern: positions
        for pattern, positions in patterns.items()
        if len(positions) > 1
    }


def calculate_distances(repeated_patterns):
    """Calculate distances between repeated pattern occurrences."""
    distances = []

    for positions in repeated_patterns.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                distances.append(positions[j] - positions[i])

    return distances


def find_factors(distances):
    """Count factors appearing in the Kasiski distances."""
    factor_count = Counter()

    for distance in distances:
        for factor in range(2, distance + 1):
            if distance % factor == 0:
                factor_count[factor] += 1

    return factor_count


def kasiski_analysis(ciphertext):
    """Perform Kasiski examination."""
    repeated_patterns = find_repeated_patterns(ciphertext)
    distances = calculate_distances(repeated_patterns)
    factors = find_factors(distances)

    candidates = [
        factor
        for factor, count in factors.most_common()
        if factor <= 20
    ]

    return candidates, repeated_patterns, distances, factors


def calculate_ic(text):
    """Calculate Index of Coincidence (bonus)."""
    n = len(text)

    if n <= 1:
        return 0.0

    counts = Counter(text)

    numerator = sum(
        count * (count - 1)
        for count in counts.values()
    )

    return numerator / (n * (n - 1))


def split_into_groups(ciphertext, key_length):
    """Split ciphertext according to the candidate key length."""
    return [
        ciphertext[i::key_length]
        for i in range(key_length)
    ]


def frequency_analysis(group):
    """Return A-Z frequency counts for a group."""
    counts = Counter(group)

    return {
        chr(ord('A') + i): counts.get(chr(ord('A') + i), 0)
        for i in range(26)
    }


def find_shift(group):
    """Find the most likely Caesar shift using chi-square analysis."""
    n = len(group)

    if n == 0:
        return 0

    observed = [
        group.count(chr(ord('A') + i))
        for i in range(26)
    ]

    best_shift = 0
    best_score = float('inf')

    for shift in range(26):
        chi_square = 0

        for plaintext_letter in range(26):

            cipher_letter = (plaintext_letter + shift) % 26

            expected = n * ENGLISH_FREQ[plaintext_letter]

            if expected > 0:
                chi_square += (
                    (observed[cipher_letter] - expected) ** 2
                ) / expected

        if chi_square < best_score:
            best_score = chi_square
            best_shift = shift

    return best_shift


def find_key(groups):
    """Combine Caesar shifts from all groups into the Vigenere key."""
    key = ""

    for group in groups:
        shift = find_shift(group)
        key += chr(ord('A') + shift)

    return key


def vigenere_decrypt(ciphertext, key):
    """Decrypt ciphertext using the recovered Vigenere key."""
    plaintext = ""

    for i, char in enumerate(ciphertext):

        cipher_value = ord(char) - ord('A')
        key_value = ord(key[i % len(key)]) - ord('A')

        plain_value = (cipher_value - key_value) % 26

        plaintext += chr(ord('A') + plain_value)

    return plaintext


def vigenere_encrypt(plaintext, key):
    """Encrypt plaintext using the Vigenere key."""
    ciphertext = ""

    for i, char in enumerate(plaintext):

        plain_value = ord(char) - ord('A')
        key_value = ord(key[i % len(key)]) - ord('A')

        cipher_value = (plain_value + key_value) % 26

        ciphertext += chr(ord('A') + cipher_value)

    return ciphertext


def verify(plaintext, key, original_ciphertext):
    """Check whether re-encryption matches the original ciphertext."""
    encrypted = vigenere_encrypt(plaintext, key)
    return encrypted == original_ciphertext


def display_frequency_table(groups):
    """Display A-Z frequency table for every group."""

    for i, group in enumerate(groups):

        frequencies = frequency_analysis(group)

        print(f"\nGroup {i + 1}")
        print("-" * 25)

        for letter, count in frequencies.items():
            print(f"{letter}: {count}")


# =========================================================
# MAIN PROGRAM
# =========================================================

ciphertext = """
QRBAI UWYOK ILBRZ XTUWL EGXSN VDXWR XMHXY FCGMW
WWSME LSXUZ

MKMFS BNZIF YEIEG RFZRX WKUFA XQEDX DTTHY NTBRJ
LHTAI KOCZX

QHBND ZIGZG PXARJ EDYSJ NUMKI FLBTN HWISW NVLFM
EGXAI AAWSL

FMHXR SGRIG HEQTU MLGLV BRSIL AEZSG XCMHT OWHFM
LWMRK HPRFB

ELWGF RUGPB HNBEM KBNVW HHUEA KILBN BMLHK XUGML
YQKHP RFBEL

EJYNV WSIJB GAXGO TPMXR TXFKI WUALB RGWIE GHWHG
AMEWW LTAEL

NUMRE UWTBL SDPRL YVRET LEEDF ROBEQ UXTHX ZYOZB
XLKAC KSOHN

VWXKS MAEPH IYQMM FSECH RFYPB BSQTX TPIWH GPXQD
FWTAI KNNBX

SIYKE TXTLV BTMQA LAGHG OTPMX RTXTH XSFYG WMVKH
LOIVU ALMLD

LTSYV WYNVW MQVXP XRVYA BLXDL XSMLW SUIOI IMELI
SOYEB HPHNR

WTVUI AKEYG WIETG WWBVM VDUMA EPAUA KXWHK MAUPA
MUKHQ PWKCX

EFXGW WSDDE OMLWL NKMWD FWTAM FAFEA MFZBN WIHYA
LXRWK MAMIK

GNGHJ UAZHM HGUAL YSULA ELYHJ BZMSI LAILH WWYIK
EWAHN PMLBN

NBVPJ XLBEF WRWGX KWIRH XWWGQ HRRXW IOMFY CZHZL
VXNVI OYZCM

YDDEY IPWXT MMSHS VHHXZ YEWNV OAOEL SMLSW KXXFX
STRVI HZLEF

JXDAS FIE
"""


ciphertext = clean_ciphertext(ciphertext)


print("=" * 70)
print("VIGENERE CIPHER CRYPTANALYSIS")
print("=" * 70)

print("\nCiphertext length:", len(ciphertext))


# ---------------------------------------------------------
# KASISKI EXAMINATION
# ---------------------------------------------------------

candidates, repeated, distances, factors = kasiski_analysis(ciphertext)

print("\nKASISKI ANALYSIS")
print("-" * 70)

print("Repeated patterns found:", len(repeated))

print("\nCandidate key lengths:")

for candidate in candidates[:10]:
    print(candidate, end=" ")

print("\n")

print("Most common factors:")

for factor, count in factors.most_common(10):
    print(f"{factor}: {count}")


# Kasiski is the PRIMARY method.
key_length = candidates[0]

print("\nEstimated Key Length:", key_length)


# ---------------------------------------------------------
# SPLIT INTO GROUPS
# ---------------------------------------------------------

groups = split_into_groups(ciphertext, key_length)


# ---------------------------------------------------------
# BONUS: INDEX OF COINCIDENCE
# ---------------------------------------------------------

print("\n")
print("=" * 70)
print("BONUS: INDEX OF COINCIDENCE")
print("=" * 70)

for i, group in enumerate(groups):

    ic = calculate_ic(group)

    print(f"Group {i + 1}: {ic:.4f}")


# ---------------------------------------------------------
# FREQUENCY ANALYSIS
# ---------------------------------------------------------

print("\n")
print("=" * 70)
print("FREQUENCY ANALYSIS")
print("=" * 70)

display_frequency_table(groups)


# ---------------------------------------------------------
# FIND KEY
# ---------------------------------------------------------

key = find_key(groups)

print("\nRecovered Key:", key)


# ---------------------------------------------------------
# DECRYPT
# ---------------------------------------------------------

plaintext = vigenere_decrypt(ciphertext, key)

print("\n")
print("=" * 70)
print("RECOVERED PLAINTEXT")
print("=" * 70)

print(plaintext)


# ---------------------------------------------------------
# VERIFICATION
# ---------------------------------------------------------

print("\n")
print("=" * 70)
print("VERIFICATION")
print("=" * 70)

if verify(plaintext, key, ciphertext):

    print("SUCCESS")
    print("Re-encryption matches the original ciphertext.")

else:

    print("FAILED")
    print("Re-encryption does NOT match the original ciphertext.")