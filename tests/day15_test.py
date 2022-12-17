from solutions.Day15.solution import get_input, get_data, get_no_beacon_for_row, p2


def test_p1():
    lines = get_input("solutions/Day15/sample")
    map, distances, *_ = get_data(lines)
    p1_result = get_no_beacon_for_row(map, distances, row=10)
    assert p1_result == 26


def test_p2():
    lines = get_input("solutions/Day15/sample")
    _, distances, *_ = get_data(lines)
    p2_result = p2(distances, 20)
    assert p2_result == 56000011
