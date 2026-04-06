from collections import defaultdict
from functools import cache

from aocd import get_data

input = get_data(day=11, year=2025).splitlines()


# WRITE YOUR SOLUTION HERE
def build_graph(lines):
    graph = defaultdict(list)
    for line in lines:
        device, outputs = line.split(": ")
        for out in outputs.split():
            graph[device].append(out)
    graph_frozen = defaultdict(tuple, {k: tuple(v) for k, v in graph.items()})
    return graph_frozen


def make_counter(graph):
    @cache
    def count(u, target):
        if u == target:
            return 1
        return sum(count(v, target) for v in graph[u])

    return count


def part_1(lines):
    graph = build_graph(lines)
    count = make_counter(graph)
    return count("you", "out")


def part_2(lines):
    graph = build_graph(lines)
    count = make_counter(graph)
    svr_dac_fft_out = count("svr", "dac") * count("dac", "fft") * count("fft", "out")
    svr_fft_dac_out = count("svr", "fft") * count("fft", "dac") * count("dac", "out")
    return svr_dac_fft_out + svr_fft_dac_out


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
