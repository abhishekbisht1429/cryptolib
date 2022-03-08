import os
import sys

import fl_hash

BLOCK_SIZE = fl_hash.BLOCK_SIZE

CONSTANT = bytes([154, 65, 244, 233, 71, 51, 24, 56, 91, 25, 204, 155, 122, 27,
                  210, 249, 234, 18, 111, 83, 11, 96, 228, 222, 119, 23, 66, 17,
                  123, 30,
                  47, 243, 215, 200, 105, 117, 12, 33, 190, 99, 181, 193, 185,
                  34,
                  176, 245, 118, 190, 167, 184, 172, 128, 143, 153, 21, 168, 34,
                  219, 253, 1, 111, 249, 136, 12, 174, 140, 89, 224, 157, 92,
                  224,
                  191, 241, 81, 123, 24, 215, 136, 223, 98, 245, 22, 33, 49,
                  192,
                  165, 64, 132, 153, 218, 155, 163, 206, 255, 179, 213, 121,
                  137,
                  138, 114, 93, 110, 0, 48, 192, 78, 246, 223, 219, 236, 2, 151,
                  234, 251, 110, 24, 230, 233, 48, 130, 237, 151, 53, 77, 88,
                  82,
                  27, 118, 147, 9, 171, 209, 87, 146, 99, 1, 100, 84, 198, 112,
                  119,
                  104, 229, 212, 99, 4, 23, 214, 145, 122, 217, 55, 84, 45, 147,
                  145,
                  2, 202, 67, 184, 8, 254, 94, 227, 252, 244, 151, 34, 199, 231,
                  181,
                  199, 107, 56, 229, 223, 75, 35, 2, 157, 115, 99, 22, 102, 63,
                  127,
                  249, 228, 230, 14, 54, 251, 30, 135, 223, 52, 192, 94, 25,
                  167, 86,
                  178, 81, 244, 2, 5, 33, 249, 230, 114, 145, 73, 255, 221, 225,
                  147,
                  81, 23, 226, 121, 218, 188, 14, 199, 115, 107, 40, 220, 74,
                  230,
                  55, 254, 33, 113, 21, 137, 95, 206, 54, 135, 198, 156, 109,
                  118,
                  190, 161, 125, 214, 149, 134, 90, 216, 50, 232, 29, 130, 138,
                  18,
                  49, 183, 0, 32, 39, 145, 202, 199, 145, 178, 239, 58, 128,
                  195,
                  107, 44, 225, 68, 166, 93, 8, 183, 121, 147, 245, 165, 153,
                  21,
                  156, 134, 221, 3, 212, 168, 205, 3, 20, 10, 158, 7, 103, 198,
                  98,
                  164, 1, 74, 18, 204, 224, 246, 170, 83, 36, 233, 197, 193, 23,
                  140,
                  75, 13, 116, 177, 71, 144, 192, 7, 224, 65, 230, 60, 244, 150,
                  121,
                  177, 37, 2, 158, 175, 157, 37, 4, 156, 119, 237, 198, 206,
                  179, 2,
                  113, 192, 6, 124, 78, 31, 106, 22, 227, 234, 169, 30, 118, 41,
                  21,
                  127, 64, 37, 96, 8, 8, 62, 69, 175, 166, 167, 139, 246, 141,
                  171,
                  58, 34, 101, 213, 114, 227, 69, 100, 137, 38, 219, 27, 109,
                  25,
                  108, 180, 107, 162, 108, 12, 60, 66, 158, 111, 236, 44, 30,
                  72,
                  216, 223, 240, 23, 130, 23, 56, 173, 228, 3, 34, 110, 57, 13,
                  192, 64, 45, 180, 163, 1, 53, 119, 199, 191, 30, 197, 55, 149,
                  166, 85, 76, 129, 72, 157, 250, 103, 228, 27, 86, 29, 150,
                  143,
                  13, 25, 189, 98, 218, 167, 191, 59, 237, 45, 20, 147, 52, 105,
                  132,
                  128, 175, 214, 225, 213, 91, 89, 251, 21, 63, 16, 253, 131,
                  105,
                  210, 105, 21, 109, 85, 138, 122, 159, 139, 203, 60, 229, 41,
                  163,
                  3, 28, 117, 251, 42, 161, 173, 112, 85, 100, 127, 221, 131,
                  243,
                  92, 204, 134, 24, 89, 226, 211, 236, 247, 236, 35, 33, 102,
                  69,
                  63, 250, 17, 134, 91, 201, 171, 47, 9, 21, 219, 254, 116, 201,
                  228, 215, 58, 52, 224, 154, 97, 118, 231, 97, 229, 36, 231,
                  21,
                  195, 218, 199, 169, 219, 131, 115, 233, 117, 49, 11, 155, 231,
                  183, 119, 96, 60, 209, 245, 35, 119, 39, 154, 154, 102, 33,
                  94,
                  32, 205, 205, 20, 74, 121, 94, 212, 133, 120, 128, 52, 114,
                  199,
                  183, 210, 45, 77, 106, 231, 71, 184, 199, 249, 230, 237, 46,
                  81,
                  55, 107, 219, 43, 170, 147, 163, 214, 168, 25, 5, 148, 95, 55,
                  245,
                  220, 54, 81, 249, 253, 68, 168, 179, 210, 132, 7, 113, 134,
                  67,
                  107, 153, 118, 49, 16, 72, 105, 88, 179, 193, 234, 109, 247,
                  243,
                  167, 136, 25, 116, 124, 185, 142, 236, 177, 165, 170, 235, 55,
                  14,
                  116, 64, 109, 10, 135, 245, 63, 44, 254, 215, 233, 92, 76,
                  254,
                  46, 231, 225, 177, 54, 45, 151, 59, 217, 78, 10, 53, 200, 50,
                  42,
                  229, 254, 184, 120, 169, 11, 235, 79, 44, 157, 158, 188, 185,
                  130, 184, 172, 123, 171, 118, 125, 202, 61, 201, 159, 200, 57,
                  63, 25, 229, 44, 89, 22, 148, 100, 154, 190, 188, 26, 100, 78,
                  62, 11, 20, 224, 79, 39, 66, 207, 233, 80, 184, 233, 109, 146,
                  141, 227, 158, 172, 234, 213, 125, 234, 98, 238, 85, 251, 187,
                  123, 234, 141, 52, 223, 51, 101, 141, 73, 237, 83, 237, 73,
                  50,
                  193, 165, 253, 140, 199, 143, 130, 62, 243, 155, 190, 233,
                  150,
                  140, 95, 119, 100, 223, 38, 50, 119, 197, 64, 122, 116, 167,
                  25,
                  64, 27, 13, 188, 92, 173, 225, 110, 117, 121, 213, 179, 1, 73,
                  156, 74, 174, 55, 128, 152, 40, 39, 9, 184, 200, 96, 205, 158,
                  192, 177, 86, 47, 137, 189, 5, 182, 231, 10, 9, 73, 103, 70,
                  216, 16, 87, 150, 243, 225, 42, 41, 168, 87, 224, 144, 7, 85,
                  9, 150, 237, 8, 225, 117, 13, 216, 15, 34, 134, 170, 97, 167,
                  196, 139, 122, 235, 152, 24, 38, 131, 210, 192, 248, 162, 105,
                  26, 21, 235, 201, 160, 153, 215, 38, 48, 217, 44, 240, 72, 71,
                  116, 90, 71, 195, 218, 138, 239, 59, 107, 83, 161, 252, 228,
                  250,
                  234, 134, 159, 201, 202, 116, 78, 70, 202, 158, 142, 89, 76,
                  201,
                  30, 106, 189, 228, 42, 137, 253, 151, 100, 106, 34, 170, 165,
                  241,
                  107, 44, 235, 233, 140, 144, 108, 246, 241, 189, 2, 4, 243,
                  238,
                  243, 210, 107, 218, 150, 78, 86, 215, 11, 207, 222, 148, 27,
                  188,
                  189, 176, 166, 132, 17, 110, 8, 188, 146, 227, 56, 28, 149,
                  30,
                  189, 192, 198, 55, 52, 16, 35, 58, 231, 31, 98, 14, 105, 226,
                  231,
                  137, 66, 251, 156, 20, 192, 26, 7, 131, 162, 89, 183, 174,
                  202, 32,
                  150, 46, 8, 3, 7, 24, 18, 154, 204, 206, 188, 62, 222, 159,
                  151,
                  74, 132, 103, 63])

IV = CONSTANT[:BLOCK_SIZE]


def md_hash(x):
    """
    calculates hash of input x using Merkle Damgard
    :param x: bytes
    :return:
    """

    n_pad = BLOCK_SIZE - (len(x) % BLOCK_SIZE)
    x = bytes(n_pad) + x

    res = IV

    for i in range(0, len(x), BLOCK_SIZE):
        x_part = x[i:i + BLOCK_SIZE]
        res_int = fl_hash.fl_hash(int.from_bytes(res, sys.byteorder),
                                  int.from_bytes(x_part, sys.byteorder))
        res = res_int.to_bytes(BLOCK_SIZE, sys.byteorder)

    return res


if __name__ == '__main__':
    message = b'Hello I am Abhishekfdasfhasdgkldfshgkldjfhglkasndjfglkjdfghl' \
              b';oajsdhfowhefgldsjkfhgnowerrgnxcvnalsdfkhowptheognmlx' \
              b';cbnospedngl;asdng;ldfsnjgoerhrtgjposndgvldf;kgnofhas' \
              b';ldfnmopdgnoerthjodsnfgldnfgl;angohopthjpdsognvA' \
              b';SLDFMAOFJPQWOJFASLJD;SBNCLBN;LDNFDASPO' \
              b';FWOETIJPOGJSDFOSDGOGERQPADVDSLFGJF;JER ' \
              b'OSODIFJSOLDFJHHEW;LSJDFL;JGHNA;SDLGHJ;DSFGJH;DFJH;HJAS;DLGHF' \
              b';OASLJHF;AOSDHFO;ASDJFHADFASFASDFHSADGHASDFIGHADSFGHASIDGPAHD'
    message_hash = md_hash(message)

    print(message_hash)
    print(len(message_hash))