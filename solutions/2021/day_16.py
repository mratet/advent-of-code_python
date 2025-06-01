from aocd import get_data
from dataclasses import dataclass

input = get_data(day=16, year=2021)

BITSTREAM = "110100101111111000101000"


def parse_header(current_i):
    packet_version = int(BITSTREAM[current_i : current_i + 3], 2)
    current_i += 3
    type_id = int(BITSTREAM[current_i : current_i + 3], 2)
    current_i += 3
    return current_i, packet_version, type_id


def read_value(current_i):
    num = ""
    while BITSTREAM[current_i] == "1":
        num += BITSTREAM[current_i + 1 : current_i + 5]
        current_i += 5
    num += BITSTREAM[current_i + 1 : current_i + 5]
    current_i += 5
    return int(num, 2)


def decode_packet(current_i):
    current_i, packet_version, type_id = parse_header(current_i)
    if type_id == 4:
        current_i, value = read_value(current_i)
        current_i += 1e9  # adjust padding
    else:
        lenght_type_id = BITSTREAM[current_i]
        current_i += 1
        if lenght_type_id == "0":
            packet_length = int(BITSTREAM[current_i : current_i + 15], 2)
            current_i += 15
            current_i = decode_packet(current_i)
        else:
            nb_packet = int(BITSTREAM[current_i : current_i + 11], 2)
            current_i += 11
            packet_count = 0
            while packet_count < nb_packet:
                current_i = decode_packet(current_i)
                packet_count += 1

    return current_i


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return


def part_2(lines):
    return


# END OF SOLUTION
# print(f'My answer is {part_1(input)}')
# print(f'My answer is {part_2(input)}')
