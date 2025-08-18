from aocd import get_data
from math import prod

input = get_data(day=16, year=2021)

OPERATIONS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda vals: vals[0] > vals[1],
    6: lambda vals: vals[0] < vals[1],
    7: lambda vals: vals[0] == vals[1],
}


def hex_to_bin(hex_str: str) -> str:
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def parse_header(bitstream, current_i):
    packet_version = int(bitstream[current_i : current_i + 3], 2)
    current_i += 3
    type_id = int(bitstream[current_i : current_i + 3], 2)
    current_i += 3
    return current_i, packet_version, type_id


def read_value(bitstream, current_i):
    num = ""
    while bitstream[current_i] == "1":
        num += bitstream[current_i + 1 : current_i + 5]
        current_i += 5
    num += bitstream[current_i + 1 : current_i + 5]
    current_i += 5
    return current_i, int(num, 2)


def decode_packet(bitstream, current_i):
    current_i, packet_version, type_id = parse_header(bitstream, current_i)
    version_sum = packet_version
    child_values = []

    if type_id == 4:
        current_i, value = read_value(bitstream, current_i)
    else:
        length_type_id = bitstream[current_i]
        current_i += 1
        if length_type_id == "0":
            packet_length = int(bitstream[current_i : current_i + 15], 2)
            current_i += 15
            subpackets_end = current_i + packet_length
            while current_i < subpackets_end:
                current_i, sum_child_ver, child_val = decode_packet(
                    bitstream, current_i
                )
                version_sum += sum_child_ver
                child_values.append(child_val)
        else:
            nb_packet = int(bitstream[current_i : current_i + 11], 2)
            current_i += 11
            for _ in range(nb_packet):
                current_i, sum_child_ver, child_val = decode_packet(
                    bitstream, current_i
                )
                version_sum += sum_child_ver
                child_values.append(child_val)

        value = OPERATIONS[type_id](child_values)

    return current_i, version_sum, value


_, total_version_sum, final_value = decode_packet(hex_to_bin(input), 0)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return total_version_sum


def part_2(lines):
    return final_value


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
