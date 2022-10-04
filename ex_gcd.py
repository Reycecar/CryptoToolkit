"""
@Author Reyce Salisbury
Extended Euclidean Algorithm program
9/29/2022
"""
import os
import sys

def egcd(a,b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = egcd(b % a, a)

    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

def main():
    op_sys = os.name
    if op_sys == "nt":
        os.system("cls")
    else:
        os.system("clear")

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except IndexError:
        print("This program requires at least 2 arguments!")

    gcd, x, y = egcd(a, b)  # use above algorithm
    
    print(f"{x} = {a}^-1 mod {b}")
    if x < 0:  # Check if x needs to be calibrated and print calibrated value
        print(f"CALIBRATED:\n\t{b + x} = {a}^-1 mod {b}")
    print(f"{y} = {b}^-1 mod {a}")
    if y < 0:  # Check if y needs to be calibrated and print calibrated value
        print(f"CALIBRATED:\n\t{a + y} = {b}^-1 mod {a}")
    print(f"gcd({a}, {b}) = {gcd}") 

    input()  # hang shell

if __name__ == '__main__':
    main()
