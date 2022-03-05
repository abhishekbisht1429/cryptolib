import cpa_secure as cpa
import mac


def gen(n) -> tuple:
    """
    Generates a key
    :param n:  security parameter (length of key in bytes)
    :return: key selected uniformly at random with length n
    """
    return (cpa.gen(n), cpa.gen(n))


def encrypt(n, k1, k2, m) -> bytes:
    """
    Encryptes message m using key k in CCA secure manner
    :param n: int, security parameter (number of bytes in a block)
    :param k1: bytes, secret key for encryption
    :param k2: bytes, secret key for mac
    :param m: bytes, message as a bytes object
    :return: bytes, cipher text
    """
    cpa_cipher = cpa.encrypt(n, k1, m)

    tag = mac.mac(n, k2, cpa_cipher)

    return cpa_cipher + tag


def decrypt(n, k1, k2, c) -> bytes:
    cpa_cipher = c[:-n]
    tag = c[-n:]
    if mac.vrfy(n, k2, cpa_cipher, tag):
        return cpa.decrypt(n, k1, cpa_cipher)
    else:
        return bytes()

if __name__ == '__main__':
    message = b'Hello I am Abhishek Bisht'
    n = 16
    k1, k2 = gen(n)

    print("message: ", message)
    cipher = encrypt(n, k1, k2, message)
    print("Cipher: ", cipher)
    decrypted = decrypt(n, k1, k2, cipher)
    print("decrypted: ", decrypted)


