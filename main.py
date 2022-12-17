from solutions.Day1.solution import day1
from solutions.Day2.solution import day2
from solutions.Day3.solution import day3
from solutions.Day4.solution import day4
from solutions.Day5.solution import day5
from solutions.Day6.solution import day6
from solutions.Day7.solution import day7
from solutions.Day8.solution import day8
from solutions.Day9.solution import day9
from solutions.Day10.solution_v2 import day10
from solutions.Day11.solution import day11
from solutions.Day12.solution import day12
from solutions.Day13.solution import day13
from solutions.Day14.solution import day14
from solutions.Day15.solution import day15
from solutions.Day16.solution import day16

days = [
    day1,
    day2,
    day3,
    day4,
    day5,
    day6,
    day7,
    day8,
    day9,
    day10,
    day11,
    day12,
    day13,
    day14,
    day15,
    day16,
]

if __name__ == "__main__":
    for day in days:
        print(f"============= Day {days.index(day) + 1} =============")
        day()
        print()
