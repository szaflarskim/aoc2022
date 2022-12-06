from string import ascii_lowercase, ascii_uppercase

f = open("Day3/input", "r")
lines = [line.rstrip() for line in f]
f.close()


def get_priorities():
    priorities = {}
    for value, c in enumerate(ascii_lowercase, start=1):
        priorities[c] = value
    for value, c in enumerate(ascii_uppercase, start=27):
        priorities[c] = value
    return priorities


def get_rucksacks():
    rucksacks = [(r[0 : len(r) // 2], r[len(r) // 2 :]) for r in lines]
    return rucksacks


def part_1():
    priorities_value = 0
    p = get_priorities()
    r = get_rucksacks()

    for c1, c2 in r:
        i = set(c1).intersection(set(c2))
        for val in i:
            priorities_value += p[val]

    print(priorities_value)


def part_2():
    p = get_priorities()
    p_val = 0
    for i in range(0, len(lines), 3):
        same_types = set(lines[i]).intersection(lines[i + 1]).intersection(lines[i + 2])
        for val in same_types:
            p_val += p[val]
    print(p_val)


def day3():
    part_1()
    part_2()
