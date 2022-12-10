
def get_input(input_file):
    input_file = open(input_file, "r")
    lines = [line.rstrip() for line in input_file]
    input_file.close()
    return lines


def get_dir_size(
    lines,
    next_index=0,
    current_path=None,
    dir_sizes=None,
):
    if next_index == 0:
        current_path = []
        dir_sizes = {}
    current_dir = current_path[-1::][0] if len(current_path) > 0 else None
    if current_dir and current_dir not in dir_sizes:
        dir_sizes["_".join(current_path)] = []
    while next_index < len(lines):
        line = lines[next_index]
        tokens = line.split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    return (next_index, dir_sizes)
                else:
                    next_index, dir_sizes = get_dir_size(
                        lines,
                        next_index + 1,
                        current_path=current_path + [tokens[2]],
                        dir_sizes=dir_sizes,
                    )
                    if current_dir:
                        dir_sizes["_".join(current_path)].append(
                            sum(dir_sizes["_".join(current_path + [tokens[2]])])
                        )
        elif tokens[0].isnumeric():
            dir_sizes["_".join(current_path)].append(int(tokens[0]))
        next_index = next_index + 1
    return next_index, dir_sizes


def p1(lines):
    _, dirs = get_dir_size(lines)
    less_than_100000 = [
        sum(dirs[dir_name]) for dir_name in dirs.keys() if sum(dirs[dir_name]) <= 100000
    ]
    print(f"The sum of their total sizes is: {sum(less_than_100000)}")


def p2(lines):
    _, dirs = get_dir_size(lines)
    total_space = 70000000
    required = 30000000

    all_dir_sizes = sum(dirs["/"])
    need_to_release = required - (total_space - all_dir_sizes)
    size_match = [
        sum(dirs[dir_name])
        for dir_name in dirs.keys()
        if sum(dirs[dir_name]) > need_to_release
    ]
    print(f"Smallest matching dir size: {min(size_match)}")


def day7(input_file="Day7/sample"):
    p1(get_input(input_file=input_file))
    p2(get_input(input_file=input_file))


# day7('aoc2022-inputs/d7')
