import math
import operator


def get_lines(input_file):
    f = open(input_file, "r")
    lines = [line.rstrip() for line in f]
    f.close()
    return lines


def get_test_function(divisor):
    def test(num):
        return int(num) % int(divisor) == 0

    return test


def get_operation(operation):
    op, num = operation
    op = operator.add if op == "+" else operator.mul

    def operation(old, mod, stressed):
        result = op(int(old), int(num) if num.isnumeric() else int(old))
        return result % mod if stressed else result

    return operation


def relief_worry(num):
    return str(int(num) // 3)


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
                num for num in line.split("Starting items: ")[1].split(", ")
            ]
        elif "Operation: new = " in line:
            current_monkey["op"] = get_operation(line.split()[-2:])
        elif "Test: divisible by " in line:
            div = line.split()[-1]
            current_monkey["test_val"] = int(div)
            current_monkey["test"] = get_test_function(div)
        elif "If true: " in line:
            current_monkey["on_true"] = int(line.split()[-1])
        elif "If false" in line:
            current_monkey["on_false"] = int(line.split()[-1])
    return monkeys


def monkeys_turn(monkeys, monkey_no, mod, stressed=False):
    if len(monkeys[monkey_no]["items"]) == 0:
        # skip when monkey has no items
        return
    current_monkey = monkeys[monkey_no]

    for item in current_monkey["items"]:
        current_monkey["inspections"] += 1
        worry_level = current_monkey["op"](item, mod, stressed)
        if not stressed:
            worry_level = relief_worry(worry_level)
        if current_monkey["test"](worry_level):
            monkeys[current_monkey["on_true"]]["items"].append(str(worry_level))
        else:
            monkeys[current_monkey["on_false"]]["items"].append(str(worry_level))

    # all items thrown
    current_monkey["items"] = []


def monkeys_rounds(monkeys, rounds_num, stressed=False):
    mod = math.lcm(*[m["test_val"] for m in monkeys])
    for _ in range(0, rounds_num):
        for monkey_no in range(0, len(monkeys)):
            monkeys_turn(monkeys, monkey_no, mod, stressed)


def get_monkey_business(lines, rounds_no, stressed=False):
    monkeys = get_monkeys(lines)
    monkeys_rounds(monkeys, rounds_no, stressed)
    inspections = [m["inspections"] for m in monkeys]
    return math.prod(sorted(inspections)[-2:])


def day11(input_file="Day11/sample"):
    lines = get_lines(input_file)
    monkey_business = get_monkey_business(lines, 20)
    print(f"Monkey business for part 1: {monkey_business}")

    monkey_business = get_monkey_business(lines, 10000, stressed=True)
    print(f"Monkey business for part 2: {monkey_business}")


def test():
    lines = get_lines("Day11/sample")
    assert get_monkey_business(lines, 20) == 10605
    assert get_monkey_business(lines, 10000, stressed=True) == 2713310158


# day11("aoc2022-inputs/d11")

# test()
