def get_input(input_file):
    input_file = open(input_file, "r")
    lines = [line.rstrip() for line in input_file]
    input_file.close()
    return lines


def get_sorted_elves(lines):
    elves = [[]]

    for cal in lines:
        if cal:
            elves[len(elves) - 1].append(int(cal))
        else:
            elves.append([])
    elves = [sum(elf) for elf in elves]
    elves.sort(reverse=True)
    return elves


def day1(input_file="src/Day1/sample"):
    sorted_elves = get_sorted_elves(get_input(input_file=input_file))
    # Sol 1
    print(f"Most calories carried {sorted_elves[0]}")

    # Sol 2
    print(f"Top three calories: {sum(sorted_elves[:3])}")


def test():
    sorted_elves = get_sorted_elves(get_input(input_file="src/Day1/sample"))
    assert sorted_elves[0] == 24000
    assert sum(sorted_elves[:3]) == 24000 + 11000 + 10000


# test()

if __name__ == "__main__":
    day1()
    # day1('aoc2022-inputs/d1')
