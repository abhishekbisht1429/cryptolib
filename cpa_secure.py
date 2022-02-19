import prf
import random


def gen(n):
    """
    Generates a key
    :param n:  security parameter (length of key)
    :return: key selected uniformly at random with length n
    """
    return random.getrandbits(n)


def encrypt(n, k, m):
    """
    Encryptes message m using key k
    :param n: security parameter
    :param k: secret key
    :param m: message
    :return: cipher text
    """
    # random number for probabilistic encryption
    r = gen(n)

    res = prf.pf(n, r, k)

    c = (res ^ m) ^ (r << n)

    return c


def decrypt(n, k, c):
    """
    Decrypt cipher text c using key k
    :param n: security parameter
    :param k: secret key
    :param c: ciphertext
    :return: plaintext
    """
    mask = (1 << n) - 1

    r = (mask << n) & c
    s = mask & c

    m = prf.pf(n, r, k) ^ s

    return m


if __name__ == '__main__':
    message = int(input("Message "))

    n = 32
    k = gen(n)

    cipher1 = encrypt(n, k, message)
    print("Cipher1", cipher1)

    cipher2 = encrypt(n, k, message)
    print("Cipher2", cipher2)

    plain1 = decrypt(n, k, cipher1)
    print("Plain", plain1)

    plain2 = decrypt(n, k, cipher2)
    print("Plain", plain2)
