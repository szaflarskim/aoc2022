from collections import defaultdict
from copy import deepcopy
import re
from queue import Queue

"""
All Valves begin closed;

One minute to open valve
One minute to walk between valves

"""


class Valve:
    def __init__(self, name, flow_rate, neighbors=[]):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = neighbors
        self.paths = dict()

    def get_shortest_path(self, target, valve_map):
        if target in self.paths:
            return self.paths[target]
        queue = Queue()
        queue.put(self.name)
        source = dict()
        source[self] = None

        while not queue.empty():
            here = queue.get()

            if here == target:
                break

            for neighbor in valve_map[here].neighbors:
                if neighbor not in source:
                    queue.put(neighbor)
                    source[neighbor] = here

        current = target
        shortest_path = []
        while current != self.name:
            shortest_path.append(current)
            try:
                current = source[current]
            except:
                self.paths[target] = None
                return None
        shortest_path.append(current)
        valve_map[target].paths[self.name] = shortest_path
        self.paths[target] = list(reversed(shortest_path))
        return self.paths[target]

    def get_shortest_path_length(self, target, valve_map):
        path = self.get_shortest_path(target, valve_map)
        if path is None:
            return None
        return len(path) - 1


def get_input(input_file):
    f = open(input_file, "r")
    lines = [line.rstrip() for line in f]
    f.close()
    return lines


def get_valve_map(lines):
    valve_map = dict()
    first_valve = ""
    for i, line in enumerate(lines):
        name_str, flow_rate, neighbors_str = [v for v in re.split("=|;", line)]
        flow_rate = int(flow_rate)
        name = name_str.split()[1]
        if i == 0:
            first_valve = name
        neighbors = re.split(" |, ", neighbors_str)[5:]
        valve_map[name] = Valve(name, flow_rate, neighbors)
    return valve_map, first_valve


def get_most_pressure(start, valve_map, max_time=30):
    queue = Queue()
    queue.put([0, (), start, 0])
    visited = set()
    max_pressure = 0

    while not queue.empty():
        time_passed, opened, current_valve, pressure_released = queue.get()
        if time_passed >= max_time:
            max_pressure = max(max_pressure, pressure_released)
            continue

        if (opened, current_valve) in visited:
            continue
        visited.add((opened, current_valve))

        opened_valves_pressure_released = pressure_released
        for valve in opened:
            opened_valves_pressure_released += valve_map[valve].flow_rate

        if valve_map[current_valve].flow_rate > 0 and current_valve not in opened:
            queue.put(
                [
                    time_passed + 1,
                    tuple(list(opened) + [current_valve]),
                    current_valve,
                    opened_valves_pressure_released,
                ]
            )

        for neighbor in valve_map[current_valve].neighbors:
            queue.put(
                [time_passed + 1, opened, neighbor, opened_valves_pressure_released]
            )
    return max_pressure


def p1(input_file="solutions/Day16/sample"):
    lines = get_input(input_file)
    valve_map, first_valve = get_valve_map(lines)

    most_pressure = get_most_pressure(first_valve, valve_map)
    print(f"Most pressure released {most_pressure}")


def p2(input_file="solutions/Day16/sample"):
    lines = get_input(input_file)
    valve_map, first_valve = get_valve_map(lines)

    most_pressure = get_most_pressure(first_valve, valve_map, max_time=26, p2=True)


def day16(input_file="solutions/Day16/sample"):
    p1(input_file)


def test():
    lines = get_input("solutions/Day16/sample")
    print(lines)


if __name__ == "__main__":
    day16()
    day16("aoc2022-inputs/d16")  # 1641
# test()
