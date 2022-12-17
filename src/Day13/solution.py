import json

from enum import Enum


class CompResult(Enum):
    THE_GOOD = 1
    THE_BAD = 2
    THE_UGLY = 3


def load_json(packet_pair):
    return [json.loads(string) for string in packet_pair]


def get_packets(input_file):
    f = open(input_file, "r")
    raw_packet_pairs = f.read().split("\n\n")
    packets_json = [[[2]], [[6]]]
    for packet_pair in raw_packet_pairs:
        left, right = packet_pair.split("\n")
        packets_json.append(json.loads(left))
        packets_json.append(json.loads(right))
    f.close()

    return packets_json


def get_packet_pairs(input_file):
    f = open(input_file, "r")
    raw_packet_pairs = f.read().split("\n\n")
    packet_pairs = [pair.split("\n") for pair in raw_packet_pairs]
    packet_pairs_json = [load_json(packet) for packet in packet_pairs]
    f.close()
    return packet_pairs_json


def compare_lists(left, right):
    list_in_right_order = CompResult.THE_UGLY

    for i in range(min([len(left), len(right)])):
        l_item = left[i]
        r_item = right[i]
        compare_result = compare_pair([l_item, r_item])
        if compare_result is CompResult.THE_BAD:
            list_in_right_order = CompResult.THE_BAD
            break
        elif compare_result is CompResult.THE_GOOD:
            list_in_right_order = CompResult.THE_GOOD
            break

    if list_in_right_order in [CompResult.THE_GOOD, CompResult.THE_BAD]:
        return list_in_right_order
    elif list_in_right_order is CompResult.THE_UGLY:
        if len(left) < len(right):
            return CompResult.THE_GOOD
        elif len(left) > len(right):
            return CompResult.THE_BAD
        else:
            return CompResult.THE_UGLY


def compare_int(left, right):
    if left < right:
        return CompResult.THE_GOOD
    elif left > right:
        return CompResult.THE_BAD
    else:
        return CompResult.THE_UGLY


def compare_pair(packet_pair):
    left, right = packet_pair
    if isinstance(left, int) and isinstance(right, int):
        return compare_int(left, right)
    elif isinstance(left, list) and isinstance(right, list):
        return compare_lists(left, right)
    else:
        left = [left] if isinstance(left, int) else left
        right = [right] if isinstance(right, int) else right
        return compare_lists(left, right)


def get_indices_in_right_order(packet_pairs):
    already_right_order = []
    for i, pair in enumerate(packet_pairs, start=1):
        if compare_pair(pair) is not CompResult.THE_BAD:
            already_right_order.append(i)
    return already_right_order


def bubble_sort_packets(packets):
    # 0.17s user 0.02s system 72% cpu 0.271 total for p1 and p2 on full input
    for i in range(len(packets)):
        for j in range(0, len(packets) - i - 1):
            if compare_pair([packets[j], packets[j + 1]]) is CompResult.THE_BAD:
                packets[j], packets[j + 1] = packets[j + 1], packets[j]
    return packets


def quick_sort_packets(packets):
    """
    # 0.03s user 0.02s system 39% cpu 0.129 total for p1 and p2 on full input
    """
    if len(packets) <= 1:
        return packets
    pivot = packets[0]
    left = []
    right = []
    for packet in packets[1:]:
        if compare_pair([packet, pivot]) is not CompResult.THE_BAD:
            left.append(packet)
        else:
            right.append(packet)
    return quick_sort_packets(left) + [pivot] + quick_sort_packets(right)


def get_divider_indices(packets, print_packages=False):
    # packets = bubble_sort_packets(packets)
    packets = quick_sort_packets(packets)

    index = 0
    divider_1_index = None
    divider_2_index = None
    while divider_1_index is None or divider_2_index is None:
        if packets[index] == [[2]]:
            divider_1_index = index + 1
        if packets[index] == [[6]]:
            divider_2_index = index + 1
        index += 1
    if print_packages:
        print("Sorted packets: ")
        for packet in packets:
            print(packet)

    return divider_1_index, divider_2_index


def p1(input_file="src/Day13/sample"):
    packet_pairs = get_packet_pairs(input_file)
    already_right_order = get_indices_in_right_order(packet_pairs)
    print(f"Already in right order sum: {sum(already_right_order)}")


def p2(input_file="src/Day13/sample"):
    packets = get_packets(input_file)
    divider_1_index, divider_2_index = get_divider_indices(packets)

    print(f"Product of divider indices: {divider_1_index * divider_2_index}")


def day13(input_file="src/Day13/sample"):
    p1(input_file)
    p2(input_file)


def test_already_sorted():
    packet_pairs = get_packet_pairs("src/Day13/sample")
    already_right_order = get_indices_in_right_order(packet_pairs)
    print(already_right_order)
    assert already_right_order == [1, 2, 4, 6]


def test_divider_indices():
    packets = get_packets("src/Day13/sample")
    divider_1_index, divider_2_index = get_divider_indices(packets, print_packages=True)
    assert divider_1_index == 10
    assert divider_2_index == 14


def test():
    test_already_sorted()
    test_divider_indices()



if __name__ == "__main__":
    day13()
# day13("aoc2022-inputs/d13")

# test()
