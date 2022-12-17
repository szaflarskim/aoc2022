from solutions.Day14.solution import get_input, get_cave, sand_flow


def test_part1():
    lines = get_input("solutions/Day14/sample")
    cave, *min_max = get_cave(lines)
    assert sand_flow(cave, *min_max) == 24


def test_part2():
    lines = get_input("solutions/Day14/sample")
    cave, *min_max = get_cave(lines)
    assert sand_flow(cave, *min_max, part2=True) == 93
