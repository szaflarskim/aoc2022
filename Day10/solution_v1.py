def get_instructions(input_file):
    f = open(input_file, "r")
    instructions = [line.rstrip() for line in f]
    f.close()
    return instructions


def clock_tick(current_cycle, x_reg, signal_strength_values):
    current_cycle += 1

    if (current_cycle - 20) % 40 == 0:
        signal_strength_values.append(x_reg * current_cycle)
    return current_cycle


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
    signal_strength_values = []
    screen = []

    for instruction in instructions:
        draw_screen(screen, current_cycle, x_reg)
        inst = instruction.split()
        op = inst[0]
        if op == "addx":
            current_cycle = clock_tick(current_cycle, x_reg, signal_strength_values)
            draw_screen(screen, current_cycle, x_reg)
            x_reg += int(inst[1])

        current_cycle = clock_tick(current_cycle, x_reg, signal_strength_values)

    return signal_strength_values, screen


def day10(input_file="Day10/sample2"):
    instructions = get_instructions(input_file)
    sum_of_signal_strengths, screen = process_instructions(instructions)
    print(f"Sum of signal strengths: {sum(sum_of_signal_strengths)}")
    print("".join(screen))


# day10("aoc2022-inputs/d10")
