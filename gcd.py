'''
@Author Reyce Salisbury
9/29/2022
'''
import sys
import math

def gcd(p, q):
    if (q == 0):
        return abs(p)
    else:
        return gcd(q, p % q)
        
def main():
    try:
        p = int(sys.argv[1])
        q = int(sys.argv[2])
    except IndexError:
        print("This program requires at least two arguments!")
    ans = gcd(p, q)
    print(ans)
    input()  # hang shell

if __name__ == "__main__":
    main()