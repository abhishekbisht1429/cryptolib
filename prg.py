"""Generator for PRNG"""
GENERATOR = 3

"""Prime number for PRNG"""
PRIME = 7


def generate(seed, out_len=None):
    """Generates a pseudo random value from the input seed"""
    if out_len is None:
        k = 2 * seed.bit_length()
    else:
        k = 2 * out_len
    x = seed
    output = 0
    for i in range(0, k):
        x = pow(GENERATOR, x, PRIME)
        # print("x ", x)
        if x >= ((PRIME - 1) / 2):
            output |= (1 << i)

    return output


# if __name__ == '__main__':
#     # seed = int(input("Seed: "))
#     for seed in range(0, 100):
#         val = generate(seed)
#         print(seed, val, bin(val))
