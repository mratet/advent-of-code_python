from aocd import get_data
input = get_data(day=13, year=2015).splitlines()
import re, collections, itertools

def _parse(input):
    graph = collections.defaultdict(dict)
    pattern = re.compile(r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.")

    for line in input:
        nom1, action, valeur, nom2 = pattern.findall(line)[0]
        graph[nom1][nom2] = int(valeur) * (1 if action == "gain" else -1)
    return graph

def compute_hapiness(graph):
    n = len(graph)
    arrangements = list(itertools.permutations(graph.keys()))
    total_changed = []
    for arrangement in arrangements:
        changed = sum(
            graph[v][arrangement[(i + 1) % n]] + graph[v][arrangement[i - 1]] for i, v in enumerate(arrangement))
        total_changed.append(changed)
    return max(total_changed)

def part_1(input):
    graph = _parse(input)
    return compute_hapiness(graph)

def part_2(input):
    graph = _parse(input)
    guest = list(graph.keys())

    for v in guest:
        graph['me'][v] = 0
        graph[v]['me'] = 0

    return compute_hapiness(graph)


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
