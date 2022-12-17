from solutions.Day5.solution import get_input, p1, p2


def test_part_1():
    lines = get_input(input_file="solutions/Day5/sample")
    assert p1(lines) == "CMZ"


def test_part_2():
    lines = get_input(input_file="solutions/Day5/sample")
    assert p2(lines) == "MCD"
