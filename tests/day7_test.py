from solutions.Day7.solution import get_input, p1, p2


def test_p1():
    lines = get_input(input_file="solutions/Day7/sample")
    assert p1(lines) == 95437


def test_p2():
    lines = get_input(input_file="solutions/Day7/sample")
    assert p2(lines) == 24933642
