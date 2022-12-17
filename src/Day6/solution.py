def get_input(input_file):
    input_file = open(input_file, "r")
    lines = input_file.readlines()
    input_file.close()
    return lines


def get_marker_start(buffer_stream, marker_start=4):
    partial = []
    for i, c in enumerate(buffer_stream, start=1):
        partial.append(c)
        if i >= marker_start and len(set(partial[-marker_start::1])) >= marker_start:
            return i


def get_packet_start(buffer_stream):
    return get_marker_start(buffer_stream, marker_start=4)


def get_message_start(buffer_stream):
    return get_marker_start(buffer_stream, marker_start=14)


def p1(lines):
    for line in lines:
        print(f"For {line} packet start at {get_packet_start(line)}")


def p2(lines):
    for line in lines:
        print(f"For {line} message start at {get_message_start(line)}")


def day6(input_file="src/Day6/sample"):
    p1(get_input(input_file=input_file))
    p2(get_input(input_file=input_file))

if __name__ == "__main__":
    day6()
# day6('aoc2022-inputs/d6')
