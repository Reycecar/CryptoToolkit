"""
@Author Reyce Salisbury
Find carmichael numbers using Fermat's primality test
Shows all carmichael values at or below x (located in main)
"""
import random
import multiprocessing as mp
import math
import time


def fermats(p, s):
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    
    for _ in range(s):
        a = random.randint(2, (p - 2))
        if math.gcd(p, a) == 1:  # test carmichael number
            if sq_and_mul(a, p-1, p) != 1:  # test a^(n-1) = 1 (mod n)
                return False
    return True


def sq_and_mul(a, b, mod):
    stepStr = str(bin(b))[2:]
    final = 1
    for i in range(len(stepStr)):
        final = (final ** 2) % mod
        if stepStr[i] == '1':
            final = (final * a) % mod
    return final


def test_prime(p):
    sqrt = int(p ** 0.5)
    i = 2  # init
    while i <= sqrt:
        if p % i == 0:
            return False
        i += 1
    return True


def get_carmichael(p, s):
    if fermats(p, s):
        if not test_prime(p):
            return p


def main():
    x = 100000  # number to count down from
    s = 20  # security parameter (testing = 5-10, in use = 15-20)
    
    start = time.perf_counter()
    with mp.Pool(15) as pool:
        args = [(i, s) for i in range(x, 4, -1)]
        results = list(filter(lambda val: val is not None, pool.starmap(get_carmichael, args)))
    print(results)  # prints all carmichael numbers found
    end = time.perf_counter()
    print(f"{round(end-start, 2)} seconds")

    start = time.perf_counter()
    x = 100000
    cNum = []
    while len(cNum) < 3:
        x = x - 1
        p = get_carmichael(x, s)
        if p is not None:
            cNum.append(p)
    print(cNum)  # prints all carmichael numbers found
    end = time.perf_counter()
    print(f"{round(end - start, 2)} seconds")


if __name__ == '__main__':
    main()
