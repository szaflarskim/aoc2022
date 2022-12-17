from solutions.Day3.solution import get_input, part_1, part_2


def test_part1():
    lines = get_input(input_file="solutions/Day3/sample")
    assert part_1(lines) == 157


def test_part2():
    lines = get_input(input_file="solutions/Day3/sample")
    assert part_2(lines) == 70
