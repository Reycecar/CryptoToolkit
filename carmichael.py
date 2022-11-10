"""
@Author Reyce Salisbury
Find carmichael numbers using Fermat's primality test
Shows all carmichael values at or below x (located in main)
"""
import random
import multiprocessing as mp
import math
import time

def fermats(p, S):
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    
    for _ in range(S):
        a = random.randint(2, (p - 2))
        if math.gcd(p, a) == 1:  # test carmichael number
            if sqAndMul(a, p-1, p) != 1:  # test a^(n-1) = 1 (mod n)
                return False
        
    return True

def sqAndMul(a, b, mod):
    stepstr = str(bin(b))[2:]
    final = 1
    for i in range(len(stepstr)):
        final = (final ** 2) % mod
        if stepstr[i] == '1':
            final = (final * a) % mod
    return final

def testPrime(val):
    sqrt = int(val ** 0.5)
    i = 2  # init
    while(i <= sqrt):
        if(val % i == 0):
            return False
        i += 1
    return True

def get_carm(x, S):
    if fermats(x, S):
        if not testPrime(x):
            return x

def main():
    x = 10000000  # number to count down from
    S = 20  # security parameter (testing = 5-10, in use = 15-20)
    
    start = time.perf_counter()
    with mp.Pool(15) as pool:
        args = [(i, S) for i in range(x, 4, -1)]
        results = list(filter(lambda val: val is not None, pool.starmap(get_carm, args)))
    print(results)  # prints all carmichael numbers found
    end = time.perf_counter()
    print(f"{round(end-start, 2)} seconds")

if __name__ == '__main__':
    main()