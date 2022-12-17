from string import ascii_lowercase, ascii_uppercase
from queue import Queue

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
    start_position = ()
    target_position = ()
    for x, line in enumerate(lines):
        row = []
        for y, c in enumerate(line):
            if c == "S":
                start_position = (x, y)
                row.append(ascii_lowercase.find("a"))
            elif c == "E":
                target_position = (x, y)
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
        within_map.append((start_x, start_y + 1))
    # right
    if start_x + 1 < width:
        within_map.append((start_x + 1, start_y))
    # left
    if start_x - 1 >= 0:
        within_map.append((start_x - 1, start_y))
    # down
    if start_y - 1 >= 0:
        within_map.append((start_x, start_y - 1))

    def test_point_height(here, there):
        max_height = height_map[here[0]][here[1]] + 1
        target_elevation = height_map[there[0]][there[1]]
        return target_elevation <= max_height

    can_go = [
        pos
        for pos in within_map
        if pos not in visited and test_point_height(start_position, pos)
    ]
    return can_go


# breadth first search
def get_shortest_path_bfs(height_map, start_position, target_position):
    queue = Queue()
    queue.put(start_position)
    visited = dict()
    visited[start_position] = None

    while not queue.empty():
        current_position = queue.get()
        viable_neighbors = get_viable_neighbors(height_map, current_position, visited)

        if current_position == target_position:
            break

        for neighbor in viable_neighbors:
            if neighbor not in visited:
                queue.put(neighbor)
                visited[neighbor] = current_position

    current = target_position
    shortest_path = []
    while current != start_position:
        shortest_path.append(current)
        try:
            current = visited[current]
        except KeyError:
            return None
    shortest_path.reverse()
    return shortest_path


def day12(input_file="solutions/Day12/sample"):
    lines = get_lines(input_file)
    height_map, start_position, target_position = get_height_map(lines)
    shortest_path = get_shortest_path_bfs(height_map, start_position, target_position)
    steps = len(shortest_path)
    print(f"Part 1: Shortest path takes {steps} steps.")

    shortest_trail = 1e7
    for x, row in enumerate(height_map):
        for y, _ in enumerate(height_map[x]):
            if row[y] == 0:
                path = get_shortest_path_bfs(height_map, (x, y), target_position)
                if path and len(path) < shortest_trail:
                    shortest_trail = len(path)

    print(f"Part 2: Shortest trail is {shortest_trail} steps.")


def test():
    lines = get_lines("solutions/Day12/sample")
    height_map, start_position, target_position = get_height_map(lines)
    shortest_path = get_shortest_path_bfs(height_map, start_position, target_position)
    assert len(shortest_path) == 31


if __name__ == "__main__":
    day12()
# day12("aoc2022-inputs/d12")

# test()
