from prg import generate


def g0(g):
    """extracts the left half of g"""
    s = g.bit_length() // 2
    mask = ((1 << s) - 1) << s
    return g & mask


def g1(g):
    """extracts the right half of g"""
    s = g.bit_length() // 2
    mask = ((1 << s) - 1)
    return g & mask


def pf(x, key):
    """pseudorandom function"""
    res = key
    while x > 0:
        g = generate(res, key.bit_length())
        res = g0(g) if (x & 1) == 0 else g1(g)
        x >>= 1

    return res


if __name__ == '__main__':
    # x = int(input("N: "))
    # key = int(input("key (64 bit): "))

    for x in range(0, 100):
        print(pf(x, 221))
