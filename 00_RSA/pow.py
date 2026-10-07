__author__ = "Laurin Wolf"
__date__ = "06/10/2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"

import math


def main() -> None:
    print("Main")
    print(pow(100, 1000, 100))
    print(pow(99, 999, 100))

def pow(a: float, b: int, n: int = None) -> float:
    if b < 0:
        a = 1 / a
        b = -b

    result = 1.0
    current_product = a

    while b > 0:
        if b & 1:
            result *= current_product
            if n is not None:
                result = result % n
        current_product *= current_product
        if n is not None:
            current_product = current_product % n
        b >>= 1

    return result

if __name__ == "__main__":
    main()