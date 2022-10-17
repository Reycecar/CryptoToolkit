"""
@Author Reyce Salisbury
Used for multiplying two polynomials that are represented as 8-bit hexadecimal values in GF(2^8)

ie x^4 + x^2 + x + 1 = 00010111 / 0x17

Argument 1 = poly_A
Argument 2 = poly_B

Program operation:

poly_A * poly_B % (0x1B)

Note:   0x1B is the hexadecimal representation of the AES irr. polynomial, 
        which is used to derive GF(2^8)
"""
import sys

def main():
    hexpoly_A = int(sys.argv[1], 16)
    hexpoly_B = int(sys.argv[2], 16)

    sum = 0
    while (hexpoly_B > 0):
        if (hexpoly_B & 1):
            sum = sum ^ hexpoly_A  # if last bit of b is 1, add poly_a to the sum
        hexpoly_B = hexpoly_B >> 1  # divide poly_B by 2
        hexpoly_A = hexpoly_A << 1  # multiply poly_A by 2
        if (hexpoly_A & 0x100):
            hexpoly_A = hexpoly_A ^ 0x11B  # mod poly_A by the AES irr. poly (0x11B)

    print(sum)


if __name__ == '__main__':
    main()