__author__ = "Laurin Wolf"
__date__ = "01/10/2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"

import random


def main() -> None:
    print("Testen von 2, 3, 5, 7, 11, 997 Primzahlen")
    for i in [2, 3, 5, 7, 11, 997]:
        print(str(i) + " prime? " + str(is_prime(i)))

    print()
    print("Testen von 9, 15, 21, 551 … 570, 6601, 89112^2 Zahlen")

    for i in [2, 3, 5, 7, 11, 997]:
        print(str(i) + " prime? " + str(is_prime(i)))


def is_prime(p: int) -> bool:
    """
    Prüft mit dem Fermat-Primzahltest, ob eine Zahl p (vermutlich) prim ist.
    Da der Test zufällig (probabilistisch) arbeitet, setzen wir im Doctest
    einen Seed, um das Ergebnis für zusammengesetzte Zahlen reproduzierbar zu machen.

    Beispiele:
    >>> import random
    >>> random.seed(42)
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(97)
    True
    >>> is_prime(9)
    False
    """
    a = random.randint(2, p - 1) if p > 2 else 1
    return pow(a, (p - 1), p) == 1


if __name__ == "__main__":
    main()