import hash


def hmac(m, k):
    """
    Computes HMAC of message m using key k
    :param m: bytes, message
    :param k: bytes, key
    :return:
    """
    k_len = len(k)
    ipad = bytes(b'0x5C' * k_len)
    temp = bytes([a ^ b for (a, b) in zip(ipad, k)])
    res1 = hash.md_hash(temp + m)

    opad = bytes(b'0x36' * k_len)
    temp2 = bytes([a ^ b for (a, b) in zip(opad, k)])
    res = hash.md_hash(temp2 + res1)

    return res


if __name__ == '__main__':
    res = hmac(b'adfasf', b'asdfaf')
    print(res)
    print(len(res))