from cipher_yz4286 import cipher_yz4286
import pytest

def test_cipher_with_single_wd():
    single_word = 'irene'
    assert cipher_yz4286.cipher(single_word, 2, encrypt=True) == 'ktgpg', "Using single word not pass"
