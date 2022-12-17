from string import ascii_lowercase
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


class Vertex:
    def __init__(self, height_map, position):
        self.h_map = height_map
        self.position = position
        self.elevation = height_map[position[0]][position[1]]
        self.neighbors = self.__get_viable_neighbors()

    def __get_viable_neighbors(self):
        within_map = []
        start_x, start_y = self.position
        height = len(self.h_map[0])
        width = len(self.h_map)
        # up
        if start_y + 1 < height:
            within_map.append((start_x, start_y + 1))
        # right
        if start_x + 1 < width:
            within_map.append((start_x + 1, start_y))
        # down
        if start_y - 1 >= 0:
            within_map.append((start_x, start_y - 1))
        # left
        if start_x - 1 >= 0:
            within_map.append((start_x - 1, start_y))

        def test_point_height(there):
            max_height = self.elevation + 1
            target_elevation = self.h_map[there[0]][there[1]]
            return target_elevation <= max_height

        can_go = [pos for pos in within_map if test_point_height(pos)]
        # print(f"viable neighbors from {start_position}:  {can_go}")
        return can_go


def get_shortest_path(v_map, start_position, target_position):
    """
    Breadth First Search
    """
    queue = Queue()
    queue.put(start_position)
    source = dict()
    source[start_position] = None

    while not queue.empty():
        here = queue.get()

        if here == target_position:
            break

        for neighbor in v_map[here].neighbors:
            if neighbor not in source:
                queue.put(neighbor)
                source[neighbor] = here

    current = target_position
    shortest_path = []
    while current != start_position:
        shortest_path.append(current)
        try:
            current = source[current]
        except KeyError:
            return None
    shortest_path.reverse()
    return shortest_path


def get_height_map(lines):
    height_map = []
    start_position = []
    target_position = []
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


def get_v_map(lines):
    height_map, start_position, target_position = get_height_map(lines)
    v_map = {}
    for x in range(len(height_map)):
        for y in range(len(height_map[0])):
            v_map[(x, y)] = Vertex(height_map, (x, y))
    return v_map, start_position, target_position


def day12(input_file="src/Day12/sample"):
    lines = get_lines(input_file)
    v_map, start_position, target_position = get_v_map(lines)

    shortest = get_shortest_path(v_map, start_position, target_position)
    print(f"Part 1: Shortest path takes {len(shortest)} steps.")

    shortest_trail = 1e7
    for _, point in v_map.items():
        if point.elevation == 0:
            path = get_shortest_path(v_map, point.position, target_position)
            if path and len(path) < shortest_trail:
                shortest_trail = len(path)

    print(f"Part 2: Shortest trail is {shortest_trail} steps.")


def test():
    lines = get_lines("src/Day12/sample")
    v_map, start_position, target_position = get_v_map(lines)
    shortest = get_shortest_path(v_map, start_position, target_position)
    assert len(shortest) == 31

if __name__ == "__main__":
    day12()
# day12("aoc2022-inputs/d12")

# test()
