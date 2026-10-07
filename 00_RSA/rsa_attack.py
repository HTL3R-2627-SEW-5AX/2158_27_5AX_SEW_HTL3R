__author__ = "Laurin Wolf"
__date__ = "07/10/2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"
import argparse
import math
import sys

def main() -> None:
    print("Main")



def fermat_factorization(n: int, max_attempts: int = None):
    """Faktorisiert den RSA-Modul n mittels Fermat-Faktorisierung.

    Rückgabe: (p, q, attempts)
    """
    if n <= 0:
        raise ValueError("Der Modul muss eine positive Ganzzahl sein.")

    # Wenn n gerade ist, direkt abfangen
    if n % 2 == 0:
        return 2, n // 2, 1

    # Startwert a = ceil(sqrt(n))
    a = math.isqrt(n)
    if a * a < n:
        a += 1

    attempts = 0

    while True:
        attempts += 1

        if max_attempts is not None and attempts > max_attempts:
            return None, None, attempts

        b2 = a * a - n
        b = math.isqrt(b2)

        # Prüfen, ob b2 eine perfekte Quadratzahl ist
        if b * b == b2:
            p = a - b
            q = a + b
            return p, q, attempts

        a += 1


def main():
    parser = argparse.ArgumentParser(
        description="Fermat-Angriff auf einen RSA-Modul N."
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        help="Ausführliche Ausgabe aktivieren",
    )
    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=None,
        metavar="MAX",
        help="Maximale Versuche",
    )
    parser.add_argument("modul", type=int, help="Der zu faktorisiere RSA-Modul N")

    args = parser.parse_args()

    p, q, attempts = fermat_factorization(args.modul, max_attempts=args.max)

    if p is None or q is None:
        print(
            f"Keine Faktoren innerhalb von {args.max} Versuchen gefunden.",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.verbose:
        print(
            f"Es braucht {attempts} Versuche, um die Faktoren von {args.modul} zu finden:"
        )
        print(f"p = {p}")
        print(f"q = {q}")
    else:
        print((p, q))


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()