__author__ = "Laurin Wolf"
__date__ = "01/10/2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"

import random


def main() -> None:
    print("Testen von 2, 3, 5, 7, 11, 997 Primzahlen")
    for i in [2, 3, 5, 7, 11, 997]:
        print( str(i)  + " prime? " + str(is_prime(i)))

    print()
    print("Testen von 9, 15, 21, 551 … 570, 6601, 89112^2 Zahlen")

    for i in [2, 3, 5, 7, 11, 997]:
        print( str(i)  + " prime? " + str(is_prime(i)))

def is_prime(p: int) -> bool:
    a = random.randint(2, p-1) if p > 2 else 1
    return pow(a, (p - 1), p) == 1

if __name__ == "__main__":
    main()