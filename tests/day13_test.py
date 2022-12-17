from solutions.Day13.solution import (
    get_packets,
    get_packet_pairs,
    get_indices_in_right_order,
    get_divider_indices,
)


def test_already_sorted():
    packet_pairs = get_packet_pairs("solutions/Day13/sample")
    already_right_order = get_indices_in_right_order(packet_pairs)
    print(already_right_order)
    assert already_right_order == [1, 2, 4, 6]


def test_divider_indices():
    packets = get_packets("solutions/Day13/sample")
    divider_1_index, divider_2_index = get_divider_indices(packets, print_packages=True)
    assert divider_1_index == 10
    assert divider_2_index == 14
