import os
import sys

import prf

def gen(n) -> bytes:
    """
    Generatertes random bytes of length n
    :param n: int, security parameter
    :return: bytes, bytes of length n
    """

    return os.urandom(n)

def mac(n, key, message):
    """
    computes CBC-MAC tag for message
    :param n: int, size of block in bytes
    :param key: bytes, secret key
    :param message: bytes, message for which tag is to be computed
    :return: MAC tag
    """
    # padding - PKCS5
    n_pad = n - (len(message) % n)
    for i in range(n_pad):
        message = n_pad.to_bytes(1, sys.byteorder) + message

    n_bits = n * 8

    key_int = int.from_bytes(key, sys.byteorder)

    tag = prf.pf(n_bits, len(message), key_int)
    for i in range(0, len(message), n):
        message_part_int = int.from_bytes(message[i:i+n], sys.byteorder)
        tag = tag ^ message_part_int
        tag = prf.pf(n_bits, tag, key_int)

    return tag

    # if key.bit_length() != message.bit_length():
    #     return None
    #
    # return prf.pf(key.bit_length(), message, key)


def vrfy(n, key, message, tag):
    """
    verifies if tag is valid
    :param n: int, security parameter
    :param key: bytes, secret shared key
    :param message: bytes, message to be verified with tag
    :param tag: bytes, tag for verification
    :return: True if tag is valid else False
    """

    return tag == mac(n, key, message)


if __name__ == '__main__':
    message = b'hello i am Abhishek'
    n = 8

    key = gen(n)
    tag = mac(n, key, message)
    print(tag)

    print(vrfy(n, key, message, tag))