from string import ascii_lowercase, ascii_uppercase


def get_input(input_file):
    input_file = open(input_file, "r")
    lines = [line.rstrip() for line in input_file]
    input_file.close()
    return lines


def get_priorities():
    priorities = {}
    for value, c in enumerate(ascii_lowercase, start=1):
        priorities[c] = value
    for value, c in enumerate(ascii_uppercase, start=27):
        priorities[c] = value
    return priorities


def get_rucksacks(lines):
    rucksacks = [(r[0 : len(r) // 2], r[len(r) // 2 :]) for r in lines]
    return rucksacks


def part_1(lines):
    priorities_value = 0
    p = get_priorities()
    r = get_rucksacks(lines)

    for c1, c2 in r:
        i = set(c1).intersection(set(c2))
        for val in i:
            priorities_value += p[val]

    return priorities_value


def part_2(lines):
    p = get_priorities()
    p_val = 0
    for i in range(0, len(lines), 3):
        same_types = set(lines[i]).intersection(lines[i + 1]).intersection(lines[i + 2])
        for val in same_types:
            p_val += p[val]
    return p_val


def day3(input_file="solutions/Day3/sample"):
    print(part_1(get_input(input_file=input_file)))
    print(part_2(get_input(input_file=input_file)))


if __name__ == "__main__":
    day3()
# day3('aoc2022-inputs/d3')
