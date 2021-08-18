"""Advent of code 2015 day 3."""
from collections import namedtuple, defaultdict
from typing import Dict, Tuple

Coordinate = namedtuple("Coordinate", ["x", "y"])

def parse_arrows(arrow: str) -> Coordinate:
    """Take a <>^v arrow and turn it into a vector."""
    coordinate_map = {
        "<": Coordinate(-1, 0),
        ">": Coordinate(1, 0),
        "^": Coordinate(0, 1),
        "v": Coordinate(0, -1),
    }
    return coordinate_map[arrow]


def move_sled(origin: Coordinate, vector: Coordinate) -> Coordinate:
    """Move the sled from an original coordinate along a vector."""
    x = origin.x + vector.x
    y = origin.y + vector.y
    return Coordinate(x, y)


def visit_houses(arrows: str) -> Dict[Coordinate, int]:
    """Deliver presents to all the houses you visit.

    This does more than part 1 requires, but it might be handy in part 2 and
    it's interesting to implement.
    """
    houses = defaultdict(int)
    sled_location = Coordinate(0, 0)
    houses[sled_location] += 1
    for arrow in arrows:
        vector = parse_arrows(arrow)
        sled_location = move_sled(sled_location, vector)
        houses[sled_location] += 1
    return houses

def part1(arrows: str) -> int:
    """Do part 1 of the puzzle."""
    houses = visit_houses(arrows)
    return len(houses)


EXAMPLE_1 = [
    (">", 2),
    ("^>v<", 4),
    ("^v^v^v^v^v", 2),
]

for test_input, answer in EXAMPLE_1:
    test_answer = part1(test_input)
    if test_answer != answer:
      raise ValueError(f"{test_input} didn't work, expected {answer}, got {test_answer}")

with open("input.txt", "r") as f:
  PUZZLE_IN = f.readline()

print(f"Part1: {part1(PUZZLE_IN)}")


def split_route(arrows: str) -> Tuple[str, str]:
  """Split arrows between santa and robo santa"""
  santa_arrows = arrows[::2]
  robo_santa_arrows = arrows[1::2]
  return santa_arrows, robo_santa_arrows

def part2(arrows: str) -> int:
  """Solve part 2.
  
  Man I would not have done any of this challenge like this
  if I'd known the number of houses wasn't going to matter
  """
  santa_arrows, robo_santa_arrows = split_route(arrows)
  santa_houses = visit_houses(santa_arrows)
  robo_santa_houses = visit_houses(robo_santa_arrows)
  unique_houses = set()
  for key in robo_santa_houses.keys():
    unique_houses.add(key)
  for key in santa_houses.keys():
    unique_houses.add(key)
  return len(unique_houses)

EXAMPLE_2 = [
  ("^v", 3),
  ("^>v<", 3),
  ("^v^v^v^v^v", 11)
]

for test_input, answer in EXAMPLE_2:
    test_answer = part2(test_input)
    if test_answer != answer:
      raise ValueError(f"{test_input} didn't work, expected {answer}, got {test_answer}")

print(f"Part2: {part2(PUZZLE_IN)}")
