from solutions.Day12.solution import (
    get_lines,
    get_v_map,
    get_shortest_path,
    get_shortest_trail_length,
)


def test_shortest_path():
    lines = get_lines("solutions/Day12/sample")
    v_map, start_position, target_position = get_v_map(lines)
    shortest = get_shortest_path(v_map, start_position, target_position)
    assert len(shortest) == 31


def test_shortest_trail():
    lines = get_lines("solutions/Day12/sample")
    v_map, _, target_position = get_v_map(lines)
    shortest_trail = get_shortest_trail_length(v_map, target_position)
    assert shortest_trail == 29
