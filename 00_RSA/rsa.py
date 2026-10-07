__author__ = "Laurin Wolf"
__date__ = "07/10/2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"

import argparse
import json
import random
from typing import Generator

import euklid
import miller_rabin


def generate_keys(number_of_bits: int) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    n = 0
    p = 0
    q = 0

    # HIER: != statt <= verwenden!
    while n.bit_length() != number_of_bits:
        p, q = get_p_q(number_of_bits, 10)
        n = p * q

    phi_n = (p - 1) * (q - 1)

    e = 0
    while euklid.gcd(e, phi_n) != 1:
        e = random.randrange(3, phi_n, 2)

    d = pow(e, -1, phi_n)

    return (e, n, number_of_bits), (d, n, number_of_bits)


def get_p_q(key_length: int, k: int) -> tuple[int, int]:
    half_bits = key_length // 2
    p = 0
    q = 0

    while not miller_rabin.is_prim_millerrabin(p, k) or not miller_rabin.is_prim_millerrabin(q, k) or p == q:
        p = random.randint(2**(half_bits - 1), (2**half_bits) - 1) | 1
        q = random.randint(2**(half_bits - 1), (2**half_bits) - 1) | 1

    return p, q


def file2ints(filename: str, keylen: int) -> Generator[int, None, None]:
    blocksize = (keylen // 8) - 1
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(blocksize)
            if not chunk:
                break
            yield int.from_bytes(chunk, byteorder="big")


def save_key(filename: str, key_tuple: tuple[int, int, int]) -> None:
    exp, n, keylen = key_tuple
    data = {
        "exponent": exp,
        "modulus": n,
        "keylen": keylen
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_key(filename: str) -> tuple[int, int, int]:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["exponent"], data["modulus"], data["keylen"]


def keygen_action(keylength: int, verbose: bool = False) -> None:
    if verbose:
        print(f"Generiere Schlüsselpaar ({keylength} Bits)...")
    pub_key, priv_key = generate_keys(keylength)
    save_key("public_key.json", pub_key)
    save_key("private_key.json", priv_key)


def encrypt_action(input_file: str, verbose: bool = False) -> None:
    pub_key = load_key("public_key.json")
    output_file = input_file + ".enc"

    e, n, keylen = pub_key
    with open(output_file, "w", encoding="utf-8") as out:
        for m in file2ints(input_file, keylen):
            c = pow(m, e, n)
            out.write(f"{c}\n")

    if verbose:
        print(f"Datei erfolgreich verschlüsselt: {output_file}")


def decrypt_action(input_file: str, verbose: bool = False) -> None:
    priv_key = load_key("private_key.json")
    if input_file.endswith(".enc"):
        output_file = input_file[:-4]
    else:
        output_file = input_file + ".dec"

    d, n, keylen = priv_key
    blocksize = (keylen // 8) - 1

    with open(input_file, "r", encoding="utf-8") as f_in:
        lines = [line.strip() for line in f_in if line.strip()]

    with open(output_file, "wb") as f_out:
        total_blocks = len(lines)
        for i, line in enumerate(lines):
            c = int(line)
            m = pow(c, d, n)

            # Wie viele Bytes braucht m wirklich?
            length_needed = (m.bit_length() + 7) // 8
            if length_needed == 0:
                length_needed = 1

            if i < total_blocks - 1:
                # Normaler Block: Auffüllen auf blocksize (falls m führende Nullen hatte)
                num_bytes = max(blocksize, length_needed)
            else:
                # Letzter Block: Braucht kein Padding auf blocksize
                num_bytes = length_needed

            chunk_bytes = m.to_bytes(num_bytes, byteorder="big")
            f_out.write(chunk_bytes)

    if verbose:
        print(f"Datei erfolgreich entschlüsselt: {output_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="RSA CLI Tool")
    parser.add_argument("-v", "--verbosity", action="store_true")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-k", "--keygen", type=int)
    group.add_argument("-e", "--encrypt", type=str)
    group.add_argument("-d", "--decrypt", type=str)
    group.add_argument("--test", action="store_true")


    args = parser.parse_args()

    if args.test:
        import doctest
        doctest.testmod(verbose=True)
        return

    if args.keygen:
        keygen_action(args.keygen, verbose=args.verbosity)
    elif args.encrypt:
        encrypt_action(args.encrypt, verbose=args.verbosity)
    elif args.decrypt:
        decrypt_action(args.decrypt, verbose=args.verbosity)


if __name__ == "__main__":
    main()