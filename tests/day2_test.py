from solutions.Day2.solution import (
    get_input,
    get_score,
    get_outcome_original,
    get_outcome_new_rules,
)


def test_day2():
    lines = get_input(input_file="solutions/Day2/sample")
    assert get_score(lines, get_outcome_original) == 15
    assert get_score(lines, get_outcome_new_rules) == 12
