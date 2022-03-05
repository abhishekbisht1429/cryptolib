import sys

import prf
import os


def gen(n) -> bytes:
    """
    Generates a key
    :param n:  security parameter (length of key in bytes)
    :return: key selected uniformly at random with length n
    """
    return os.urandom(n)


def encrypt(n, k, m) -> bytes:
    """
    Encryptes message m using key k
    :param n: int, security parameter (number of bytes in a block)
    :param k: int, secret key
    :param m: bytes, message as a bytes object
    :return: bytes, cipher text
    """

    # padding - PKCS5
    n_pad = n - (len(m) % n)
    for i in range(n_pad):
        m = n_pad.to_bytes(1, sys.byteorder) + m

    print(len(m))
    print("npad enc ", m[0])
    print("after pad ", m)

    # start OFB mode encryption
    iv = gen(n)  # initialization vector
    print("iv enc ", iv)
    key_int = int.from_bytes(k, sys.byteorder) # integer representation of key
    cipher = bytearray(iv)
    prf_inp_int = int.from_bytes(iv, sys.byteorder)
    for i in range(0, len(m), n):
        print(m[i:i + n])
        message_part_int = int.from_bytes(m[i:i+n], sys.byteorder)
        prf_out_int = prf.pf(n * 8, prf_inp_int, key_int)
        print("prf out int enc ", prf_out_int)

        print("message part int enc ", message_part_int)
        # xor 
        cipher_part_int = prf_out_int ^ message_part_int
        print("cipher part int enc ", cipher_part_int)

        cipher += cipher_part_int.to_bytes(n, sys.byteorder)

        prf_inp_int = prf_out_int

    # res = prf.pf(n, r, k)
    #
    # c = (res ^ m) ^ (r << n)

    return bytes(cipher)


def decrypt(n, k, c) -> bytes:
    """
    Decrypt cipher text c using key k

    :param n : int, security parameter
    :param k: bytes, secret key of length n bytes
    :param c: bytes, ciphertext
    :return: bytes, plaintext
    """

    print(len(c))
    iv = c[0:n]  # initialization vector
    print("iv dec", iv)

    message = bytearray()
    prf_inp_int = int.from_bytes(iv, sys.byteorder)
    key_int = int.from_bytes(k, sys.byteorder)
    # decrypt the cipher
    for i in range(n, len(c), n):
        prf_out_int = prf.pf(n * 8, prf_inp_int, key_int)
        print("prf out int dec ", prf_out_int)
        cipher_part_int = int.from_bytes(c[i:i+n], sys.byteorder)
        print("cipher part  int dec ", cipher_part_int)

        message_part_int = prf_out_int ^ cipher_part_int

        print("message part int dec ", message_part_int)

        print('')
        message += message_part_int.to_bytes(n, sys.byteorder)

        prf_inp_int = prf_out_int

    n_pad = message[0]
    print("npad dec ", n_pad)

    message = message[n_pad:]
    return bytes(message)
    # mask = (1 << n) - 1
    #
    # r = (mask << n) & c
    # s = mask & c
    #
    # m = prf.pf(n, r, k) ^ s
    #
    # return m


if __name__ == '__main__':
    message = b'hello, I am Abhishek Bisht. This is a casdfasdfryptolib'
    n = 32
    k = gen(n)

    print("message: ", message)
    cipher = encrypt(n, k, message)
    print("cipher: ", cipher)

    print("\n")

    decrypted = decrypt(n, k, cipher)
    print("decrypted cipher: ", decrypted)
    # message = int(input("Message "))
    #
    # n = 32
    # k = gen(n)
    #
    # cipher1 = encrypt(n, k, message)
    # print("Cipher1", cipher1)
    #
    # cipher2 = encrypt(n, k, message)
    # print("Cipher2", cipher2)

    # plain1 = decrypt(n, k, cipher1)
    # print("Plain", plain1)
    #
    # plain2 = decrypt(n, k, cipher2)
    # print("Plain", plain2)
