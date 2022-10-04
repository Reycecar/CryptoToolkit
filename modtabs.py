"""
@Author Reyce Salisbury
9/29/2022
Computes and displays all elements of (x^y mod n) where: x ∈ {1, 2, ... (n-1), n} and y ∈ {0, 1, ... (n-1)}
order = number of elements of a finite field
Runs with an integer argument (n) and optional integer argument (m).

With 1 argument:
    Will create a table with the powers of each value from from
    (1-n)^(0-n) mod n
    as well as the order of each value in that table.
    Table will indicate where the order starts to repeat.

With 2 arguments:
    Shows m^x mod n (where x is 0-n) as well as the order for m in Zn
"""

import sys


def title(n):
    print("      ", end="")
    for i in range(0, n):  # make the title
        print(str(i) + ' ' * (5 - len(str(i))), end="")
    print(" | (order)")


def make_row(m, n):
    """
    Create Rows for modtabs table
    param m: int
    param n: int
    """
    vals = {}  # dict of values to determine order of m (value:occurrences)
    starred = False
    for i in range(0, n):
        v = ((m ** i) % n)

        if v in vals.keys():
            vals[v] += 1
            if v == 1 and i != 0 and starred is False:
                print(f"{v}*   ", end="")
                starred = True
            else:
                print(str(v) + ' ' * (5 - len(str(v))), end="")
        else:
            vals[v] = 1
            print(str(v) + ' ' * (5 - len(str(v))), end="")

    if vals[1] > 1:
        order = len(vals)
    else:  # if (m^i mod n) never equals 1 (aside from when i=0), order is undefined.
        order = "UND"

    print(f" |    {order}", end="")
    print()


def main():
    a = len(sys.argv)

    if a > 3:
        print("Too many arguments.")

    if a == 1:
        print("You must run this program with arguments!")

    if a == 2:
        n = int(sys.argv[1])
        print(f"POWERS MOD {n}")
        title(n)
        for i in range(1, n):
            print(' ' * (abs(len(str(i)) - 2)) + f"{i}|   ", end="")
            make_row(i, n)

    if a == 3:
        n = int(sys.argv[1])
        m = int(sys.argv[2])

        print(f"POWERS OF {m} MOD {n}")
        title(n)
        print(f"{m}|" + ' ' * (5 - len(str(m))), end="")
        make_row(m, n)

    input()  # Hang the Shell


if __name__ == "__main__":
    main()
