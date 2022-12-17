from solutions.Day1.solution import get_sorted_elves, get_input


def test_day1():
    sorted_elves = get_sorted_elves(get_input(input_file="solutions/Day1/sample"))
    assert sorted_elves[0] == 24000
    assert sum(sorted_elves[:3]) == 24000 + 11000 + 10000
