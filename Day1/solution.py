elves = []
current_elf = {"id": 1, "calories": 0}


def get_input(input_file):
    input_file = open(input_file, "r")
    lines = [line.rstrip() for line in input_file]
    input_file.close()
    return lines


def add_elf():
    global elves, current_elf
    elves.append(current_elf)
    current_elf = {"id": current_elf["id"] + 1, "calories": 0}


def get_sorted_elves(lines):
    global elves, current_elf
    for cal in lines:
        if not cal:
            add_elf()
        else:
            current_elf["calories"] = current_elf["calories"] + int(cal)

    # last elf
    add_elf()

    sorted_elves = sorted(elves, key=lambda elf: elf["calories"], reverse=True)
    return sorted_elves


def day1(input_file="Day1/sample"):
    sorted_elves = get_sorted_elves(get_input(input_file=input_file))
    # Sol 1
    print(
        f"Top calories elf {sorted_elves[0]['id']} carries {sorted_elves[0]['calories']}"
    )

    # Sol 2
    print(f"Top three calories: {sum([elf['calories'] for elf in sorted_elves[:3]])}")

# day1('aoc2022-inputs/d1')
