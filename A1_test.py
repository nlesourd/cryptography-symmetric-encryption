import pytest

import A1 as module


def test_vigenere_cipher():
    """Test of row transposition cipher with example of the lecture 3."""

    key = "deceptive"
    plaintext = "wearediscoveredsaveyourself"
    assert module.vigenere_cipher(plaintext, key) == "ZICVTWQNGRZGVTWAVZHCQYGLMGJ".lower()


def test_vigenere_decipher():
    """Test of vigenere decipher."""

    cipher = "jeteewvsvbvxeewhsbagvuaitpmfaoryhhrlrly"
    plaintext = "wearediscoveredusingchapgptsaveyourself"
    key = "nat"
    assert module.vigenere_decipher(cipher,key) == plaintext

def test_row_transposition_cipher():
    """Test of row transposition cipher with example of the lecture 3."""

    key = "4312567"
    cipher = "TTNAAPTMTSUOAODWCOIXKNLYPETZ".lower()
    plaintext = "attackpostponeduntiltwoamxyz"
    assert module.row_transposition_cipher(plaintext, key) == cipher

def test_row_transposition_decipher():
    """Test of transposition decipher with example of the lecture 3."""

    cipher = "TTNAAPTMTSUOAODWCOIXKNLYPETZ".lower()
    plaintext = "attackpostponeduntiltwoamxyz"
    key = "4312567"
    assert module.row_transposition_decipher(cipher,key) == plaintext