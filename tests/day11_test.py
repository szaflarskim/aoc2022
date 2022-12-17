from solutions.Day11.solution import get_lines, get_monkey_business


def test_monkey_business_calm():
    lines = get_lines("solutions/Day11/sample")
    assert get_monkey_business(lines, 20) == 10605


def test_monkey_business_stressed():
    lines = get_lines("solutions/Day11/sample")
    assert get_monkey_business(lines, 10000, stressed=True) == 2713310158
