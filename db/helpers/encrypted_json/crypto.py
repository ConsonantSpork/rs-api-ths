from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter


__all__ = ['encrypt', 'decrypt']


def _get_aes(key, iv=None):
    if iv is None:
        iv = Random.new().read(AES.block_size)
    iv_int = int.from_bytes(iv, 'big')
    ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)
    return AES.new(key, AES.MODE_CTR, counter=ctr), iv


def encrypt(key, plaintext):
    """Encrypt plaintext using key.

    Parameters
    ----------
    key : bytes
        key to use for encryption
    plaintext : str
        message to encrypt

    Returns
    -------
    str
        encrypted message
    """

    aes, iv = _get_aes(key)
    ciphertext = aes.encrypt(plaintext.encode())
    return iv + ciphertext


def decrypt(key, ciphertext):
    """Decrypt cipher using key.

    Parameters
    ----------
    key : bytes
        key to use for decryption
    ciphertext : bytes
        message to decrypt

    Returns
    -------
    str
        decrypted message
    """

    iv, ciphertext = ciphertext[:AES.block_size], ciphertext[AES.block_size:]
    aes, iv = _get_aes(key, iv)
    plaintext = aes.decrypt(ciphertext)
    return plaintext.decode()
