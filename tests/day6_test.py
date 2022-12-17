from solutions.Day6.solution import get_message_start, get_packet_start


def test_get_packet_start():
    assert get_packet_start("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert get_packet_start("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert get_packet_start("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert get_packet_start("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert get_packet_start("zcfzfwzzqfrljwzlrfnpqdbhtmscgvj") == 11


def test_get_message_start():
    assert get_message_start("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert get_message_start("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert get_message_start("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert get_message_start("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert get_message_start("zcfzfwzzqfrljwzlrfnpqdbhtmscgvj") == 26
