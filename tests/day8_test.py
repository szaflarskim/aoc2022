from solutions.Day8.solution import (
    get_highest_scenic_score,
    get_tree_map,
    get_visible_trees,
)


def test_get_visible_trees():
    tree_map = get_tree_map(input_file="solutions/Day8/sample")
    assert len(get_visible_trees(tree_map)) == 5


def test_scenic_score():
    tree_map = get_tree_map(input_file="solutions/Day8/sample")
    highest_score, best_tree = get_highest_scenic_score(tree_map)
    passed = [highest_score == 8, best_tree == "[3,2]"]
    assert all(passed)
