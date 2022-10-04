'''
@Author Reyce Salisbury
9/29/2022
'''
import os
import sys
import math
op_sys = os.name
if op_sys == "nt":
    os.system("cls")
else:
    os.system("clear")

try:
    p = int(sys.argv[1])
    q = int(sys.argv[2])
except IndexError:
    print("This program requires at least two arguments!")

ans = math.gcd(p, q)
print(ans)
input()  # hang shell
