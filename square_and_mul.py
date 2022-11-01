"""
@Author Reyce Salisbury
Uses the square and multiply algorithm to provide a
systematic way for finding the sequence in which to perform
squarings and multiplications by A for computing A^B mod C.

Argument 1 = A (int)
Argument 2 = B (int)
Argument 3 = C (int)

Program computes: A**B % C
"""
import sys


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    modval = int(sys.argv[3])
    stepstr = str(bin(b))[2:]
    
    final = 1
    for i in range(len(stepstr)):
        final = (final ** 2) % modval
        if stepstr[i] == '1':
            final = (final * a) % modval

    print(f"\n{a}^{b} % {modval} = {final}")


if __name__ == '__main__':
    main()