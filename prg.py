"""
Generator for PRNG.
Prime number for PRNG. Taken from
https://datatracker.ietf.org/doc/html/rfc3526
"""

# GENERATOR = 3

# PRIME = 7

# PRIME = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
#             "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
#             "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
#             "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
#             "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
#             "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F"
#             "83655D23DCA3AD961C62F356208552BB9ED529077096966D"
#             "670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF", 16)
# GENERATOR = 2


# PRIME = int("155251809230070893513091813125848175563133404943451431320235"
#             "119490296623994910210725866945387659164244291000768028886422"
#             "915080371891804634263272761303128298374438082089019628850917"
#             "0691316593175367469551763119843371637221007210577919")
# GENERATOR = 22

PRIME = 34319
GENERATOR = 4


def generate(seed, out_len=None):
    """Generates a pseudo random value from the input seed"""
    if out_len is None:
        k = 2 * seed.bit_length()
    else:
        k = 2 * out_len
    x = seed
    output = 0
    threshold = ((PRIME - 1) // 2)
    for i in range(0, k):
        x = pow(GENERATOR, x, PRIME)
        # print("x ", x)
        if x >= threshold:
            output |= (1 << i)

    return output


# if __name__ == '__main__':
#     # seed = int(input("Seed: "))
#     # print(pow(GENERATOR, 100, PRIME))
#     for seed in range(0, 100):
#         val = generate(seed)
#         print(seed, val, bin(val))
