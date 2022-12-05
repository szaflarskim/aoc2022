import re

f = open("Day5/input", "r")
lines = [line.replace("\n", "") for line in f]
f.close()


def get_stacks(stack_piles):
    stacks = {}
    columns = stack_piles.pop()
    stacks_num = int(columns[len(columns) - 1])

    for i in range(1, stacks_num + 1):
        stacks[i] = []

    for level in reversed(stack_piles):
        stack_no = 1
        for i in range(1, len(level), 4):
            if level[i].isalpha():
                stacks[stack_no].append(level[i])
            stack_no += 1
    return stacks


def get_data():
    instructions = [
        [int(inst) for inst in re.split("move|from|to", l)[1::]]
        for l in lines
        if "move" in l
    ]
    stacks = get_stacks([l for l in lines if "move" not in l and l != ""])

    return (stacks, instructions)


def crate_mover_9000(stacks, move, from_stack, to_stack):
    for _ in range(move):
        stacks[to_stack].append(stacks[from_stack].pop())


def crate_mover_9001(stacks, move, from_stack, to_stack):
    stacks[to_stack] = stacks[to_stack] + stacks[from_stack][-move::]
    del stacks[from_stack][-move:]


def execute_instructions(crate_mover, stacks, instructions):
    for inst in instructions:
        (move, from_stack, to_stack) = inst
        crate_mover(stacks, move, from_stack, to_stack)
    return stacks


def get_top_crates(crate_mover):
    stacks, instructions = get_data()
    arranged_stacks = execute_instructions(crate_mover, stacks, instructions)
    return "".join(
        [arranged_stacks[stack_no][-1] for stack_no in list(arranged_stacks.keys())]
    )


def p1():
    print(get_top_crates(crate_mover_9000))


def p2():
    print(get_top_crates(crate_mover_9001))


def day5():
    p1()
    p2()
