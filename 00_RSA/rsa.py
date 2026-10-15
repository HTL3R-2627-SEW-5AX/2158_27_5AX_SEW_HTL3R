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
    """
    Prüft mit dem Miller-Rabin-Primzahltest, ob eine Zahl n (vermutlich) prim ist.
    Da der Test probabilistisch arbeitet, setzen wir im Doctest einen Seed,
    um das Ergebnis reproduzierbar zu machen.

    Beispiele:
    >>> import random
    >>> random.seed(42)
    >>> is_prim_millerrabin(2, 5)
    True
    >>> is_prim_millerrabin(3, 5)
    True
    >>> is_prim_millerrabin(97, 5)
    True
    >>> is_prim_millerrabin(9, 5)
    False
    """
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
    """
    Teilt n - 1 so oft wie möglich durch 2, bis der Rest d ungerade ist.
    Gibt das Paar (d, r) zurück, sodass n - 1 = d * 2^r gilt.

    Beispiele:
    >>> find_powers_of_2_in_n_minus_1(9)
    (1, 3)
    >>> find_powers_of_2_in_n_minus_1(10)
    (9, 0)
    """
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    return d, r


if __name__ == "__main__":
    main()