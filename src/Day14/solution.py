from collections import defaultdict
from copy import deepcopy

# air, clay, sand_still = ".", "#", "o"
air, clay, sand_still = "⬜️", "⬛️", "🟨"


def get_input(input_file):
    f = open(input_file, "r")
    lines = [line.rstrip() for line in f]
    f.close()
    return lines


def get_min_max(cave):
    min_x, max_x = 1e7, 500
    min_y, max_y = 1e7, 0
    for x, y in cave.keys():
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)
    return min_x, max_x, min_y, max_y


def draw_cave(cave):
    min_x, max_x, min_y, max_y = get_min_max(cave)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(cave[(x, y)], end="")
        print()
    print("---------------------------------")


def get_cave(lines):
    cave = defaultdict(lambda: air)
    cave[(500, 0)] = "🟡"

    min_x, max_x = 1e7, 500
    min_y, max_y = 0, 0

    for line in lines:
        points = [p.split(",") for p in line.split(" -> ")]
        for point in range(len(points) - 1):
            x1, y1 = points[point]
            x2, y2 = points[point + 1]
            min_x, max_x = min(min_x, int(x1), int(x2)), max(max_x, int(x1), int(x2))
            min_y, max_y = min(min_y, int(y1), int(y2)), max(max_y, int(y1), int(y2))

            # vertical
            if x1 == x2:
                y1, y2 = sorted([y1, y2])
                for y in range(int(y1), int(y2) + 1):
                    cave[(int(x1), y)] = clay
            # horizontal
            else:
                x1, x2 = sorted([x1, x2])
                for x in range(int(x1), int(x2) + 1):
                    cave[(x, int(y1))] = clay
    return cave, min_x, max_x, min_y, max_y


def cave_floor(cave, *min_max):
    min_x, max_x, min_y, max_y = min_max
    min_x, max_x, min_y, max_y = min_x - 10, max_x + 10, min_y, max_y + 2

    for x in range(min_x, max_x + 1):
        cave[(x, max_y)] = clay

    return cave, min_x, max_x, min_y, max_y


def drop_sand(cave, *min_max, part2=False):
    _, _, _, max_y = min_max if min_max else get_min_max(cave)
    sand_grain = (500, 0)

    not_done = True

    while True:
        if sand_grain[1] > max_y or cave[sand_grain] == sand_still:
            not_done = False
            break

        if part2:
            for x in range(sand_grain[0] - 2, sand_grain[0] + 3):
                cave[x, max_y] = clay

        if cave[(sand_grain[0], sand_grain[1] + 1)] in [clay, sand_still]:
            if cave[(sand_grain[0] - 1, sand_grain[1] + 1)] in [clay, sand_still]:
                if cave[(sand_grain[0] + 1, sand_grain[1] + 1)] in [clay, sand_still]:
                    cave[sand_grain] = sand_still
                    break
                else:
                    sand_grain = (sand_grain[0] + 1, sand_grain[1] + 1)
            else:
                sand_grain = (sand_grain[0] - 1, sand_grain[1] + 1)
        else:
            sand_grain = (sand_grain[0], sand_grain[1] + 1)

    return not_done


def sand_flow(cave, *min_max, print_cave=False, part2=False):
    if part2:
        cave, *min_max = cave_floor(cave, *min_max)

    if print_cave:
        draw_cave(cave)

    sand_units = 0
    not_done = True
    while not_done:
        not_done = drop_sand(cave, *min_max, part2=part2)
        sand_units += 1 if not_done else 0
        if print_cave:
            draw_cave(cave)

    return sand_units


def day14(input_file="src/Day14/sample", print_cave=False):
    lines = get_input(input_file)
    cave, *min_max = get_cave(lines)
    cave_copy = deepcopy(cave)

    print("Part 1:", sand_flow(cave, *min_max, print_cave=print_cave))
    draw_cave(cave)
    print("Part 2:", sand_flow(cave_copy, *min_max, print_cave=print_cave, part2=True))
    # draw_cave(cave_copy)


def test():
    lines = get_input("src/Day14/sample")
    cave, *min_max = get_cave(lines)
    cave_copy = deepcopy(cave)
    assert sand_flow(cave, *min_max) == 24
    assert sand_flow(cave_copy, *min_max, part2=True) == 93


# day14("aoc2022-inputs/d14", print_cave=False)

if __name__ == "__main__":
    day14(print_cave=False)

# test()
