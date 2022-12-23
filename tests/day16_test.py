from solutions.Day16.solution import get_input, get_most_pressure, get_valve_map


def test_day16():
    lines = get_input("solutions/Day16/sample")
    valve_map, first_valve = get_valve_map(lines)

    most_pressure = get_most_pressure(first_valve, valve_map)
    assert most_pressure == 1651
