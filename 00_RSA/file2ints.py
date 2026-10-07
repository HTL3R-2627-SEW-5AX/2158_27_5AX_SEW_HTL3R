__author__ = "Laurin Wolf"
__date__ = "07/10/2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"

def main() -> None:
    print("Main")

from typing import Generator

def file2ints(filename: str, keylen: int) -> Generator[int, None, None]:
    blocksize = (keylen // 8) - 1

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(blocksize)
            if not chunk:
                break

            block_int = int.from_bytes(chunk, byteorder="big")
            yield block_int

if __name__ == "__main__":
    main()