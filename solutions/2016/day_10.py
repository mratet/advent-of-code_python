import collections
import re

from aocd import get_data

input = get_data(day=10, year=2016).splitlines()


def _parse(input):
    stock = collections.defaultdict(list)
    graph = collections.defaultdict(list)

    for line in input:
        if line.startswith("value"):
            _, val, *_, bot_id = line.split()
            stock["bot_" + bot_id].append(int(val))
        else:
            pattern = r"bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)"
            bot_id, type_low, low_id, type_high, high_id = re.findall(pattern, line)[0]
            graph["bot_" + bot_id].append(type_high + "_" + high_id)
            graph["bot_" + bot_id].append(type_low + "_" + low_id)
    return stock, graph


def factory_history(stock, graph, part="part_2"):
    while True:
        if all(len(value) <= 1 for value in stock.values()):
            break

        for k, v in dict(stock).items():
            if len(v) == 2:
                m, M = min(v), max(v)
                if part == "part_1" and (m, M) == (17, 61):
                    return k.removeprefix("bot_")
                stock[graph[k][0]].append(M)
                stock[graph[k][1]].append(m)
                stock[k].clear()

    return stock


def part_1(input):
    stock, graph = _parse(input)
    return factory_history(stock, graph, part="part_1")


def part_2(input):
    stock, graph = _parse(input)
    stock = factory_history(stock, graph)
    return stock["output_0"][0] * stock["output_1"][0] * stock["output_2"][0]


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
