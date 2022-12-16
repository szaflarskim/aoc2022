from collections import defaultdict
from copy import deepcopy
import re

unknown, sensor, beacon, no_beacon = "❓", "🟩", "🟨", "⬜️"


def get_input(input_file):
    f = open(input_file, "r")
    lines = [line.rstrip() for line in f]
    f.close()
    return lines


def draw_map(map, *min_max):
    min_x, max_x, min_y, max_y = min_max
    for y in range(min_y, max_y + 1):
        print(f" {y} " if y < 10 else f"{y} ", end="")
        for x in range(min_x, max_x + 1):
            print(map[(x, y)], end="")
        print()


def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_data(lines):
    map = defaultdict(lambda: unknown)
    distances = dict()

    min_x, max_x = 1e7, 0
    min_y, max_y = 1e7, 0

    for line in lines:
        _, sensor_x, sensor_y, _, beacon_x, beacon_y = [
            val for val in re.split("x=|, y=|:", line)
        ]

        sensor_x = int(sensor_x)
        sensor_y = int(sensor_y)
        beacon_x = int(beacon_x)
        beacon_y = int(beacon_y)

        min_x, max_x = min(min_x, int(sensor_x), int(beacon_x)), max(
            max_x, int(sensor_x), int(beacon_x)
        )
        min_y, max_y = min(min_y, int(sensor_y), int(beacon_y)), max(
            max_y, int(sensor_y), int(beacon_y)
        )

        map[(sensor_x, sensor_y)] = sensor
        map[(beacon_x, beacon_y)] = beacon
        distances[(sensor_x, sensor_y)] = manhattan_dist(
            (sensor_x, sensor_y), (beacon_x, beacon_y)
        )

    return map, distances, min_x, max_x, min_y, max_y


def map_no_beacon(map, distances):

    for sensor, distance in distances.items():
        distance = distances[sensor]
        for x in range(sensor[0] - distance, sensor[0] + distance + 1):
            for y in range(sensor[1] - distance, sensor[1] + distance + 1):
                if (
                    distance >= abs(sensor[0] - x) + abs(sensor[1] - y)
                    and map[(x, y)] == unknown
                ):
                    map[(x, y)] = no_beacon

    return map


def get_no_beacon_for_row(map, distances, row=10):
    count = 0
    for sensor, distance in distances.items():
        distance = distances[sensor]
        for x in range(sensor[0] - distance, sensor[0] + distance + 1):
            y = row
            if (
                distance >= abs(sensor[0] - x) + abs(sensor[1] - y)
                and map[(x, y)] == unknown
            ):
                map[(x, y)] = no_beacon
                count += 1

    return count


def p2(distances, limit):
    candidates = set()
    multiplier = 4000000

    # check along the diamond edges
    for sensor, distance in distances.items():
        sensor_x, sensor_y = sensor

        for side in range(4):
            for i in range(distance + 1):
                if side == 0:
                    x = sensor_x + distance + 1 - i
                    y = sensor_y + i
                elif side == 1:
                    x = sensor_x - distance - 1 + i
                    y = sensor_y + i
                elif side == 2:
                    x = sensor_x + distance + 1 - i
                    y = sensor_y - i
                elif side == 3:
                    x = sensor_x - distance - 1 + i
                    y = sensor_y - i

                if (x, y) not in candidates and 0 <= x <= limit and 0 <= y <= limit:
                    found = True
                    for other_sensor, dist in distances.items():
                        if manhattan_dist((x, y), other_sensor) <= dist:
                            found = False
                            break
                if found:
                    return (multiplier * x) + y
                candidates.add((x, y))
    return None


def day15(input_file="Day15/sample", p1_row=10, limit=20):
    lines = get_input(input_file)
    map, distances, *min_max = get_data(lines)

    if limit == 20:
        map_for_draw = map_no_beacon(deepcopy(map), distances)
        draw_map(map_for_draw, *min_max)

    count = get_no_beacon_for_row(map, distances, row=p1_row)
    print(f"Part 1: {count}")

    tuning_frequency = p2(distances, limit)
    if tuning_frequency:
        print("Part 2: ", tuning_frequency)
    else:
        print("Did not find tuning frequency!")


def test():
    lines = get_input("Day15/sample")
    map, distances, *_ = get_data(lines)
    p1_result = get_no_beacon_for_row(map, distances, row=10)
    assert p1_result == 26
    p2_result = p2(distances, 20)
    assert p2_result == 56000011


# day15("aoc2022-inputs/d15", p1_row=2000000, limit=4000000)

# day15()
test()
