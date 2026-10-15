__author__ = "Laurin Wolf"
__date__ = "07/10/2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"

def main() -> None:
    print("Main")

from typing import Generator

def file2ints(filename: str, keylen: int) -> Generator[int, None, None]:
    """
    Liest eine Datei blockweise im Binärmodus ein und konvertiert
    jeden Block in einen Integer (Big-Endian).

    Beispiele:
    >>> import tempfile, os
    >>> fd, path = tempfile.mkstemp()
    >>> _ = os.write(fd, b"ABC")
    >>> os.close(fd)
    >>> list(file2ints(path, 32))
    [4279875]
    >>> os.remove(path)
    """
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