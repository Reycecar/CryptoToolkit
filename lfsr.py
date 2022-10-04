"""
@author Reyce Salisbury
9/20/2022
arguments the power values of your LFSR Polynomial
    ie:
        LFSR eq = x^8+x^4+x^3+1
        so run:
        python3 lfsr.py 8 4 3 1
"""
from pylfsr import *
import sys


def construct_polynomial(numList):
    numList.sort(reverse=True)
    poly=""
    for i in numList:
        poly += "x^" + str(i) + " + "
    poly += "1"
    return poly


def greatest(numList):
    gv = numList[0]
    for num in numList:
        if num > gv:
            gv = num
    
    return gv


def main():
    fpoly = []
    for i in range(1, len(sys.argv)):
        fpoly.append(int(sys.argv[i]))

    poly_str = construct_polynomial(fpoly)
    gv = greatest(fpoly)

    initstate = []
    for i in range(0, gv):
        if i == 0:
            initstate.append(1)
        else:
            initstate.append(0)
    
    L = LFSR(initstate=initstate, fpoly=fpoly, counter_start_zero=False)

    print()
    L.info()

    print("\ncount \t state \t\t\toutbit\n" + '-'*75)
    states = {}
    for _ in range(2 ** gv):
        print(L.count,L.state,'',L.outbit,sep='\t')
        if str(L.state) not in states:
            states[str(L.state)] = 1
        else:
            states[str(L.state)] += 1
        L.next()

    print("\nOutput\n" + '-'*75 + "\n",L.seq)

    print(f"\nStates of the LFSR for {poly_str}\n" + '-'*75)
    for k,v in states.items():
        print(f"{k}:\t{v}")

    print("\nConclusion:\n" + '-'*75 + f"\nThe Period of {poly_str} is {len(states)}")

    input()


if __name__ == "__main__":
    main()
