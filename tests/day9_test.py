from solutions.Day9.solution import get_moves, process_moves


def test_moves_rope_2():
    moves = get_moves(input_file="solutions/Day9/sample2")
    tail_visited = process_moves(moves, rope_length=2, with_grid=False)
    assert len(tail_visited) == 88


def test_moves_rope_10():
    moves = get_moves(input_file="solutions/Day9/sample2")
    tail_visited = process_moves(moves, rope_length=10, with_grid=False)
    assert len(tail_visited) == 36
