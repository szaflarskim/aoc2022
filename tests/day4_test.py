from solutions.Day4.solution import get_input, p1, p2


def test_part1():
    lines = get_input(input_file="solutions/Day4/sample")
    assert p1(lines) == 2


def test_part2():
    lines = get_input(input_file="solutions/Day4/sample")
    assert p2(lines) == 4
