"""Advent of code day 4"""
import hashlib

def get_md5(str2hash: str) -> str:
    """"Get the hash of a string"""
    result = hashlib.md5(str2hash.encode())
    return result.hexdigest()


def part1(key: str, zeroes: int = 5) -> int:
    nonce = 1
    while True:
        str2hash = f"{key}{nonce}"
        lead_hash = get_md5(str2hash)[:zeroes]
        if lead_hash == "".join("0" for _ in range(zeroes)):
            return nonce
        nonce += 1

EXAMPLE_1 = [
    ("abcdef", 609043),
    ("pqrstuv", 1048970),
]

for test_input, answer in EXAMPLE_1:
    test_answer = part1(test_input)
    if test_answer != answer:
      raise ValueError(f"{test_input} didn't work, expected {answer}, got {test_answer}")

print(f"Part 1: {part1('ckczppom')}")

print(f"Part 2: {part1('ckczppom', 6)}")


