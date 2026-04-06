import collections
import itertools
import re

from aocd import get_data

input = get_data(day=13, year=2015).splitlines()


def _parse(input):
    graph = collections.defaultdict(dict)
    pattern = re.compile(r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.")

    for line in input:
        nom1, action, valeur, nom2 = pattern.findall(line)[0]
        graph[nom1][nom2] = int(valeur) * (1 if action == "gain" else -1)
    return graph


def compute_happiness(graph):
    return max(
        sum(
            graph[v][arrangement[(i + 1) % len(graph)]] + graph[v][arrangement[i - 1]]
            for i, v in enumerate(arrangement)
        )
        for arrangement in itertools.permutations(graph.keys())
    )


def part_1(input):
    graph = _parse(input)
    return compute_happiness(graph)


def part_2(input):
    graph = _parse(input)
    guest = list(graph.keys())

    for v in guest:
        graph["me"][v] = 0
        graph[v]["me"] = 0

    return compute_happiness(graph)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
