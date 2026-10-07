__author__ = "Laurin Wolf"
__date__ = "07/10/2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"

def main() -> None:
    print("Main")

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    main()