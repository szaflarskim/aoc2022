def get_instructions(input_file):
    f = open(input_file, "r")
    instructions = [line.rstrip() for line in f]
    f.close()
    return instructions


def draw_screen(screen, current_cycle, x_reg):
    if (current_cycle - 1) % 40 in [x_reg - 1, x_reg, x_reg + 1]:
        screen.append("🟥")
    else:
        screen.append("⬜️")

    if (current_cycle) % 40 == 0:
        screen.append("\n")


def process_instructions(instructions):
    x_reg = 1
    current_cycle = 1
    signal_strength = []

    instruction_no = 0
    add_x = False
    screen = []

    while instruction_no < len(instructions):

        draw_screen(screen, current_cycle, x_reg)

        current_instruction = instructions[instruction_no].split()

        if current_instruction[0] == "noop":
            instruction_no += 1

        elif add_x:
            x_reg += int(current_instruction[1])
            instruction_no += 1
            add_x = False
        else:
            add_x = True

        current_cycle += 1

        if (current_cycle - 20) % 40 == 0:
            signal_strength.append(x_reg * current_cycle)

    return signal_strength, screen


def day10(input_file="Day10/sample2"):
    instructions = get_instructions(input_file)
    sum_of_signal_strengths, screen = process_instructions(instructions)
    print(f"Sum of signal strengths: {sum(sum_of_signal_strengths)}")
    print("".join(screen))


# day10("aoc2022-inputs/d10")
