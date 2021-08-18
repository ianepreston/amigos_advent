from itertools import combinations
from math import prod
from typing import Tuple


def parse_line(line: str) -> Tuple[int, int, int]:
    """Read in the input.
    Comes in a format like 3x4x2 so we want to
    split on that, and then get a tuple of dimensions
    """
    return tuple(int(x) for x in line.split("x"))


def calc_side_areas(dims: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """Get areas from dimensions
    Each side has an area that is the product of 2 of length, width, or height.
    """
    return tuple(prod(pair) for pair in combinations(dims, 2))


def wrapping_area(areas: Tuple[int, int, int]) -> int:
    """Define the area of the box.
    Does not include the bonus wrapping paper
    specified in the problem
    """
    return sum(areas) * 2


def bonus_paper(areas: Tuple[int, int, int]) -> int:
    """Add in the extra paper we need."""
    return min(areas)


def paper_required(line: str) -> int:
    """Convert input dimensions to paper requirements.
    Wraps the last few functions for convenience.
    """
    dims = parse_line(line)
    areas = calc_side_areas(dims)
    return wrapping_area(areas) + bonus_paper(areas)


EXAMPLES_1 = [("2x3x4", 58), ("1x1x10", 43)]

for line_in, result in EXAMPLES_1:
    calc_result = paper_required(line_in)
    if calc_result != result:
        raise ValueError(f"Error on {line_in}, expected {result}, got {calc_result}")

with open("input.txt", "r") as f:
    part1 = sum(paper_required(line) for line in f.readlines())

print(f"Part 1: {part1}")


def min_perim(dims: Tuple[int, int, int]) -> int:
    """Calculate the perimiter of the smallest face of the present."""
    smallest_faces = sorted(dims)[:-1]
    return sum(smallest_faces) * 2


def bow_length(dims: Tuple[int, int, int]) -> int:
    """Calculate the volume of the rectangle for bow length."""
    return prod(dims)


def ribbon_required(line: str) -> int:
    """convert input dimensions to ribbon requirements."""
    dims = parse_line(line)
    return min_perim(dims) + bow_length(dims)


EXAMPLES_2 = [("2x3x4", 34), ("1x1x10", 14)]


for line_in, result in EXAMPLES_2:
    calc_result = ribbon_required(line_in)
    if calc_result != result:
        raise ValueError(f"Error on {line_in}, expected {result}, got {calc_result}")

with open("input.txt", "r") as f:
    part2 = sum(ribbon_required(line) for line in f.readlines())

print(f"Part 2: {part2}")
