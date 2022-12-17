def get_tree_map(input_file):
    input_file = open(input_file, "r")
    tree_map = [[int(t) for t in line.rstrip()] for line in input_file]
    input_file.close()
    return tree_map


def get_best_possible_tree_counts(tree_map, x, y):
    tree_map_length = len(tree_map)
    return [y, tree_map_length - 1 - x, tree_map_length - 1 - y, x]


def get_scenic_score(tree_map, x, y):
    num_trees = get_best_possible_tree_counts(tree_map, x, y)
    # print(f"Checking tree {[x,y]}")
    # print(f"Initial num_trees {num_trees}")

    # left
    for i in range(y - 1, 0, -1):
        if tree_map[x][i] >= tree_map[x][y]:
            # print(f"left higher {[x,i]}")
            num_trees[0] = y - i
            break

    # down
    for i in range(x + 1, len(tree_map)):
        if tree_map[i][y] >= tree_map[x][y]:
            # print(f"down higher {[i,y]}")
            num_trees[1] = i - x
            break

    # right
    for i in range(y + 1, len(tree_map)):
        if tree_map[x][i] >= tree_map[x][y]:
            # print(f"right higher {[x,i]}")
            num_trees[2] = i - y
            break

    # top
    for i in range(x - 1, 0, -1):
        if tree_map[i][y] >= tree_map[x][y]:
            # print(f"top higher {[i,y]}")
            num_trees[3] = x - i
            break

    scenic_score = 1
    for num in num_trees:
        scenic_score = scenic_score * num

    # print(num_trees)

    return scenic_score


def visible_left(tree_map, x, y):
    # left
    l_visible = True
    for i in range(0, y):
        if tree_map[x][i] >= tree_map[x][y]:
            l_visible = False
            break
    return l_visible


def visible_down(tree_map, x, y):
    # down
    d_visible = True
    for i in range(x + 1, len(tree_map)):
        if tree_map[i][y] >= tree_map[x][y]:
            d_visible = False
            break
    return d_visible


def visible_right(tree_map, x, y):
    # right
    r_visible = True
    for i in range(y + 1, len(tree_map[x])):
        if tree_map[x][i] >= tree_map[x][y]:
            r_visible = False
            break
    return r_visible


def visible_top(tree_map, x, y):
    # top
    t_visible = True
    for i in range(0, x):
        if tree_map[i][y] >= tree_map[x][y]:
            t_visible = False
            break

    return t_visible


def is_visible(tree_map, x, y):
    for visible in [visible_top, visible_right, visible_down, visible_left]:
        if visible(tree_map, x, y):
            return True
    return False


def get_visible_trees(tree_map):
    visible_trees = []
    for x in range(1, len(tree_map) - 1):
        for y in range(1, len(tree_map[x]) - 1):
            if is_visible(tree_map, x, y):
                visible_trees.append([x, y])
    return visible_trees


def get_highest_scenic_score(tree_map):
    highest_score = 0
    best_tree = ""
    for x in range(1, len(tree_map) - 1):
        for y in range(1, len(tree_map[x]) - 1):
            scenic_score = get_scenic_score(tree_map, x, y)
            # print(f"Scenic score of tree {[x,y]} is {scenic_score}")
            if scenic_score > highest_score:
                highest_score = scenic_score
                best_tree = f"[{x},{y}]"
    print(f"Best Tree {best_tree} with score {highest_score}")
    return


def p1(tree_map):
    border_trees = (len(tree_map) * 4) - 4
    print(f"Visible trees: {len(get_visible_trees(tree_map)) + border_trees}")


def p2(tree_map):
    get_highest_scenic_score(tree_map)


def day8(input_file="src/Day8/sample"):
    p1(get_tree_map(input_file=input_file))
    p2(get_tree_map(input_file=input_file))

if __name__ == "__main__":
    day8()
# day8("aoc2022-inputs/d8")
