from solutions.Day10.solution_v1 import get_instructions, process_instructions
from solutions.Day10.solution_v2 import process_instructions as process_instructions2


def test_day10_v1():
    instructions = get_instructions(input_file="solutions/Day10/sample2")
    sum_of_signal_strengths, _ = process_instructions(instructions)
    assert sum(sum_of_signal_strengths) == 13140


def test_day10_v2():
    instructions = get_instructions(input_file="solutions/Day10/sample2")
    sum_of_signal_strengths, _ = process_instructions2(instructions)
    assert sum(sum_of_signal_strengths) == 13140
