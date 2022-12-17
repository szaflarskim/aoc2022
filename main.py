from src.Day1.solution import day1
from src.Day2.solution import day2
from src.Day3.solution import day3
from src.Day4.solution import day4
from src.Day5.solution import day5
from src.Day6.solution import day6
from src.Day7.solution import day7
from src.Day8.solution import day8
from src.Day9.solution import day9
from src.Day10.solution_v2 import day10
from src.Day11.solution import day11
from src.Day12.solution import day12
from src.Day13.solution import day13
from src.Day14.solution import day14
from src.Day15.solution import day15
from src.Day16.solution import day16

days = [day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14, day15, day16]

if __name__ == "__main__":
    for day in days:
        print(f"============= Day {days.index(day) + 1} =============")
        day()
        print()
