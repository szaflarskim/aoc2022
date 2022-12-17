from collections import defaultdict
from copy import deepcopy
import re

"""
All Valves begin closed;

One minute to open valve
One minute to walk between valves

"""


class Valve:
    def __init__(self, name, flow_rate, tunnels=[]):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = tunnels
        self.open = False


def get_input(input_file):
    f = open(input_file, "r")
    lines = [line.rstrip() for line in f]
    f.close()
    return lines


def get_valve_map(lines):
    valve_map = dict()
    for line in lines:
        name_str, flow_rate, tunnels_str = [v for v in re.split("=|;", line)]
        flow_rate = int(flow_rate)
        name = name_str.split()[1]
        tunnels = re.split(" |, ", tunnels_str)[5:]
        valve_map[name] = Valve(name, flow_rate, tunnels)
    return valve_map


def day16(input_file="solutions/Day16/sample"):
    lines = get_input(input_file)
    valve_map = get_valve_map(lines)


def test():
    lines = get_input("solutions/Day16/sample")
    print(lines)


# day16("aoc2022-inputs/d16", p1_row=2000000, limit=4000000)

if __name__ == "__main__":
    day16()
# test()
