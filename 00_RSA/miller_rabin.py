__author__ = "Laurin Wolf"
__date__ = "01/10/2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"

import math
import random

from sympy import false


def main() -> None:
    print("Main")
    print(is_prim_millerrabin(10, 10))

def is_prim_millerrabin(n: int, k: int) -> bool:
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    d, r = find_powers_of_2_in_n_minus_1(n)
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True



def find_powers_of_2_in_n_minus_1(n):
    d= n - 1
    r=0
    while d % 2 == 0:
        d //= 2
        r+=1
    return d, r


if __name__ == "__main__":
    main()