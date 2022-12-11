from functools import reduce


def get_lines(input_file):
    f = open(input_file, "r")
    lines = [line.rstrip() for line in f]
    f.close()
    return lines


def get_test_function(divisor):
    def test(num):
        return int(num) % int(divisor) == 0

    return test


def get_operation(op_str):
    op, num = op_str.split(" ")

    def operation(old):
        if op == "*":
            return int(old) * int(num) if num.isnumeric() else int(old) * int(old)
        else:
            return int(old) + int(num) if num.isnumeric() else int(old) + int(old)

    return operation


def relief_worry(num):
    return int(num // 3)


def get_monkeys(lines):
    monkeys = []
    current_monkey = {}
    for line in lines:
        if "Monkey" in line:
            monkeys.append({"inspections": 0})
        else:
            current_monkey = monkeys[len(monkeys) - 1]

        if "Starting items" in line:
            current_monkey["items"] = [
                int(num) for num in line.split("Starting items: ")[1].split(", ")
            ]
        elif "Operation: new = " in line:
            current_monkey["op"] = get_operation(
                line.split("  Operation: new = old ")[1]
            )
        elif "Test: divisible by " in line:
            current_monkey["test"] = get_test_function(
                line.split("  Test: divisible by ")[1]
            )
        elif "If true: " in line:
            current_monkey["on_true"] = int(
                line.split("    If true: throw to monkey ")[1]
            )
        elif "If false" in line:
            current_monkey["on_false"] = int(
                line.split("    If false: throw to monkey ")[1]
            )
    return monkeys


def monkeys_turn(monkeys, monkey_no, hardcore = False):
    if len(monkeys[monkey_no]["items"]) == 0:
        # skip when monkey has no items
        return
    current_monkey = monkeys[monkey_no]

    for item in current_monkey["items"]:
        current_monkey["inspections"] += 1
        worry_level = current_monkey["op"](item)
        if not hardcore:
            worry_level = relief_worry(worry_level)
        if current_monkey["test"](worry_level):
            monkeys[current_monkey["on_true"]]["items"].append(worry_level)
        else:
            monkeys[current_monkey["on_false"]]["items"].append(worry_level)

    # all items thrown
    current_monkey["items"] = []


def monkeys_rounds(monkeys, rounds_num, hardcore = False):
    for i in range(0, rounds_num):
        if(i % 500 == 0):
            print(f"Round {i}")


        for monkey_no in range(0, len(monkeys)):
            monkeys_turn(monkeys, monkey_no, hardcore)


def get_monkey_business(lines, rounds_no, hardcore = False):
    monkeys = get_monkeys(lines)
    monkeys_rounds(monkeys, rounds_no, hardcore)
    inspections = [m["inspections"] for m in monkeys]
    most_active = sorted(inspections)[-2:]

    monkey_business = reduce((lambda x, y: x * y), most_active)

    return monkey_business


def day11(input_file="Day11/sample"):
    lines = get_lines(input_file)
    monkey_business = get_monkey_business(lines, 20)
    print(f"Monkey business for part 1: {monkey_business}")

    monkey_business = get_monkey_business(lines, 10000, hardcore=True)
    print(f"Monkey business for part 2: {monkey_business}")


def test():
    lines = get_lines("Day11/sample")
    assert get_monkey_business(lines, 20) == 10605
    assert get_monkey_business(lines, 20, hardcore=True) == 10197



day11("aoc2022-inputs/d11")
# day11(input_file="Day11/sample")

# test()
