import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from attacks.padding_oracle.src.lab_setup import create_lab
from attacks.padding_oracle.src.padding_oracle_attack import padding_oracle_attack


def test_lab_generates_valid_iv_and_ciphertext():
    iv, ciphertext, oracle = create_lab()

    assert len(iv) == 16
    assert len(ciphertext) > 0
    assert len(ciphertext) % 16 == 0
    assert callable(oracle)


def test_oracle_accepts_original_ciphertext():
    iv, ciphertext, oracle = create_lab()

    assert oracle(iv + ciphertext) is True


def test_attack_recovers_plaintext():
    iv, ciphertext, oracle = create_lab()

    plaintext, queries = padding_oracle_attack(
        iv, ciphertext, oracle
    )

    assert plaintext == b"Padding oracle attacks are educational."
    assert queries > 0


def test_attack_does_not_need_key_argument():
    import inspect

    parameters = inspect.signature(
        padding_oracle_attack
    ).parameters

    assert len(parameters) == 3