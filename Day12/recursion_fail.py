from string import ascii_lowercase, ascii_uppercase

"""
# a - z : elevation from lowest to highest
# S : current position at elevation a
# E : best signal location at elevation z

#  Find shortest route from S -> E, moving one square any direction, elevation gain at most one per step

e.g. for map
Sabqponm           v..v<<<<
abcryxxl           >v.vv<<^
accszExk     =>    .>vv>E^^
acctuvwj           ..v>>>^^
abdefghi           ..>>>>>^

"""


def get_lines(input_file):
    f = open(input_file, "r")
    lines = [line.rstrip() for line in f]
    f.close()
    return lines


def get_height_map(lines):
    height_map = []
    start_position = []
    target_position = []
    for x, line in enumerate(lines):
        row = []
        for y, c in enumerate(line):
            if c == "S":
                start_position = [x, y]
                row.append(ascii_lowercase.find("a"))
            elif c == "E":
                target_position = [x, y]
                row.append(ascii_lowercase.find("z"))
            else:
                row.append(ascii_lowercase.find(c))
        height_map.append(row)
    return height_map, start_position, target_position


def get_viable_neighbors(height_map, start_position, visited):
    within_map = []
    start_x, start_y = start_position
    height = len(height_map[0])
    width = len(height_map)
    # up
    if start_y + 1 < height:
        within_map.append([start_x, start_y + 1])
    # right
    if start_x + 1 < width:
        within_map.append([start_x + 1, start_y])
    # left
    if start_x - 1 >= 0:
        within_map.append([start_x - 1, start_y])
    # down
    if start_y - 1 >= 0:
        within_map.append([start_x, start_y - 1])

    def test_point_height(here, there):
        max_height = height_map[here[0]][here[1]] + 1
        target_elevation = height_map[there[0]][there[1]]
        return target_elevation <= max_height

    can_go = [
        pos
        for pos in within_map
        if str(pos) not in visited and test_point_height(start_position, pos)
    ]
    return can_go


def find_best_path(paths):
    shortest_path = None
    shortest_path_length = 1e7
    for path in paths:
        if len(path) < shortest_path_length:
            shortest_path = path
    return shortest_path


def get_shortest_path(height_map, start_position, target_position, visited=set()):
    viable_neighbors = get_viable_neighbors(height_map, start_position, visited)
    visited.add(str(start_position))
    # print(f"viable neighbors from {start_position}:  {viable_neighbors}")
    if start_position == target_position:
        # path found
        return [target_position]
    elif len(viable_neighbors) == 0:
        # no route available
        return None
    else:
        # try possible neighbors
        possible_paths = []
        for point in viable_neighbors:
            partial_path = get_shortest_path(
                height_map, point, target_position, visited
            )
            if partial_path:
                possible_paths.append(partial_path)
        if len(possible_paths) > 0:
            return [start_position] + find_best_path(possible_paths)
        else:
            return None


def day12(input_file="Day12/sample"):
    lines = get_lines(input_file)
    height_map, start_position, target_position = get_height_map(lines)
    shortest_path = get_shortest_path(height_map, start_position, target_position)
    print(shortest_path)
    steps = len(shortest_path) - 1  # minus starting point
    print(f"Shortest path takes {steps} steps.")


def test():
    lines = get_lines("Day12/sample")
    pass


# day12("aoc2022-inputs/d12")

# test()

day12()
