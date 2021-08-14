import datetime as dt
from os import getenv
from pathlib import Path
from aocd.get import get_data

today = dt.date.today()
input_year = input("Input challenge year: ")
year = int(input_year)
if year < today.year:
    max_day = 26
elif year == today.year:
    if today.month != 12:
        raise ValueError("can't get this year's challenge until December")
    max_day = today.day + 1
else:
    raise ValueError("can't do future years")

session = getenv("AOC_SESSION")
base = Path("/data")
for day in range(1, max_day):
    print(f"Getting input for year {year}, day {day}")
    input_path = base / f"{year}" / f"{day}".zfill(2)
    input_path.mkdir(parents=True, exist_ok=True)
    puzzle_input = get_data(session=session, day=day, year=year)
    input_file = input_path / "input.txt"
    with open(input_file, "w") as file:
        file.write(puzzle_input)
