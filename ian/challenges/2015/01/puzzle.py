FLOORMAP = {"(": 1, ")": -1}

def change_floors(bracket: str) -> int:
    return FLOORMAP[bracket]

def part1(brackets: str) -> int:
    floor = 0
    for bracket in brackets:
        floor += change_floors(bracket)
    return floor

# Tests
EXAMPLES = [
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3),
]

for example, solution in EXAMPLES:
    test_solution = part1(example)
    if test_solution != solution:
        raise ValueError(f"{example} did not match {solution}, got {test_solution}")

with open("input.txt", "r") as f:
    PUZZLE_INPUT = f.readline()

solution_1 = part1(PUZZLE_INPUT)
print(f"Part 1: {solution_1}")

def part2(brackets: str) -> int:
    char_position = 1
    floor = 0
    for bracket in brackets:
        floor += change_floors(bracket)
        if floor < 0:
            return char_position
        char_position += 1
    raise ValueError("Never went to basement")

EXAMPLES2 = [
    (")", 1),
    ("()())", 5),
]
for example, solution in EXAMPLES2:
    test_solution = part2(example)
    if test_solution != solution:
        raise ValueError(f"{example} did not match {solution}, got {test_solution}")

solution_2 = part2(PUZZLE_INPUT)
print(f"Part 2: {solution_2}")
