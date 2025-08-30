from aocd import get_data
from intcode import IntcodeComputer
from collections import deque
from itertools import batched

aoc_input = get_data(day=23, year=2019)


# WRITE YOUR SOLUTION HERE
def _process_packets(computer, input_value, packets_queues):
    NAT = None
    output_buffer = computer.run(input_value)
    for destination_address, X, Y in batched(output_buffer, n=3):
        if destination_address == 255:
            NAT = (X, Y)
        else:
            packets_queues[destination_address].append((X, Y))
    return NAT


def solve(lines, part="part_1"):
    computers = [IntcodeComputer(lines) for _ in range(50)]
    packets_queus = [deque([]) for _ in range(50)]

    for i, computer in enumerate(computers):
        _process_packets(computer, [i], packets_queus)

    last_NAT, NAT = None, None

    while True:
        network_is_idle = True
        for computer, packet_queue in zip(computers, packets_queus):
            if not packet_queue:
                _process_packets(computer, [-1], packets_queus)
            else:
                network_is_idle = False
                while packet_queue:
                    NAT_received = _process_packets(
                        computer, packet_queue.popleft(), packets_queus
                    )

                    if NAT_received:
                        if part == "part_1":
                            return NAT_received[1]
                        NAT = NAT_received

        if network_is_idle:
            _process_packets(computers[0], NAT, packets_queus)
            if last_NAT == NAT and part == "part_2":
                return NAT[1]
            last_NAT = NAT


def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
