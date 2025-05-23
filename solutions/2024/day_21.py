from collections import defaultdict

from aocd import get_data, submit

input = get_data(day=21, year=2024)

from collections import deque
from itertools import product

# WRITE YOUR SOLUTION HERE
DIRS = {
    (0, 1): "v",
    (1, 0): ">",
    (0, -1): "^",
    (-1, 0): "<",
}

# Best direction mapping find by testing different values (only 16 candidates)
best_direction = {
    "AA": "",
    "A^": "<",
    "A>": "v",
    "Av": "<v",
    "A<": "v<<",
    "^A": ">",
    "^^": "",
    "^>": "v>",
    "^v": "v",
    "^<": "v<",
    ">A": "^",
    ">^": "<^",
    ">>": "",
    ">v": "<",
    "><": "<<",
    "vA": "^>",
    "v^": "^",
    "v>": ">",
    "vv": "",
    "v<": "<",
    "<A": ">>^",
    "<^": ">^",
    "<>": ">>",
    "<v": ">",
    "<<": "",
}

keypad_to_corr = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}


def flatten_nested_dictionary(d):
    def recursive_flatten(sub_d):
        if all(not isinstance(v, dict) for v in sub_d.values()):
            keys, values = zip(*sub_d.items())
            combinations = product(*[v if isinstance(v, list) else [v] for v in values])
            return [dict(zip(keys, combo)) for combo in combinations]

        result = [{}]
        for key, value in sub_d.items():
            if isinstance(value, dict):
                nested = recursive_flatten(value)
                result = [{**outer, key: inner} for outer in result for inner in nested]
            else:
                if not isinstance(value, list):
                    value = [value]
                result = [{**outer, key: v} for outer in result for v in value]
        return result

    flattened = recursive_flatten(d)
    final_result = []
    for item in flattened:

        def expand(inner):
            result = {}
            for k, v in inner.items():
                if isinstance(v, dict):
                    sub_result = expand(v)
                    for sub_k, sub_v in sub_result.items():
                        result[f"{k}{sub_k}"] = sub_v
                else:
                    result[k] = v
            return result

        final_result.append(expand(item))
    return final_result


def gen_next_sequence(sequence, mapping):
    seq = "A" + sequence
    return "".join([mapping[s1 + s2] + "A" for s1, s2 in zip(seq, seq[1:])])


def generate_shortest_paths(keypad, start, end):
    start = keypad_to_corr[start]
    end = keypad_to_corr[end]
    if start == end:
        return ["A"]
    rows, cols = len(keypad), len(keypad[0])
    forbidden = (3, 0)

    def neighbors(pos):
        r, c = pos
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) != forbidden:
                yield (nr, nc)

    queue = deque([[start]])
    visited = set()
    shortest_paths = []
    min_length = float("inf")

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == end:
            path = "".join(
                [
                    DIRS[((y2 - y1), (x2 - x1))]
                    for (x1, y1), (x2, y2) in zip(path, path[1:])
                ]
            )
            if len(path) < min_length:
                shortest_paths = [path]
                min_length = len(path)
            elif len(path) == min_length:
                shortest_paths.append(path)
            continue

        if current in visited and len(path) > min_length:
            continue
        visited.add(current)

        for neighbor in neighbors(current):
            if neighbor not in path:
                queue.append(path + [neighbor])

    return shortest_paths


def generate_keypad_mappings(code):
    K = ["789", "456", "123", ".0A"]
    Acode = "A" + code
    base_keypad_mapping = defaultdict(dict)
    for start, end in zip(Acode, Acode[1:]):
        base_keypad_mapping[start][end] = generate_shortest_paths(K, start, end)
    return flatten_nested_dictionary(base_keypad_mapping)


def find_best_keypad_mapping(code, direction):
    keypad_mappings = generate_keypad_mappings(code)
    tab = []
    for i, keypad_mapping in enumerate(keypad_mappings):
        w = gen_next_sequence(code, keypad_mapping)
        for _ in range(5):
            w = gen_next_sequence(w, direction)
        tab.append((len(w), i))
    tab.sort()
    return tab[0][1]


def part_1(lines):
    lines = lines.splitlines()
    ans = 0
    for code in lines:
        best_idx = find_best_keypad_mapping(code, best_direction)
        keypad_mapping = generate_keypad_mappings(code)[best_idx]
        w = gen_next_sequence(code, keypad_mapping)
        for _ in range(2):
            w = gen_next_sequence(w, best_direction)
        ans += int(code[:3]) * len(w)
    return ans


def get_transition_dict(direction):
    d = {}
    for v in direction.values():
        seq = "A" + v + "A"
        d[v + "A"] = [direction[m1 + m2] + "A" for m1, m2 in zip(seq, seq[1:])]
    d["A"] = ["A"]
    return d


def get_next_state(D, transition_dict):
    new_D = defaultdict(int)
    for k, c in D.items():
        for symb in transition_dict[k]:
            new_D[symb] += c
    return new_D


def part_2(lines):
    lines = lines.splitlines()
    transition_dict = get_transition_dict(best_direction)
    ans = 0
    for code in lines:
        best_idx = find_best_keypad_mapping(code, best_direction)
        keypad_mapping = generate_keypad_mappings(code)[best_idx]
        w = gen_next_sequence(code, keypad_mapping)
        w = gen_next_sequence(w, best_direction)
        D = defaultdict(int)
        for symb in w.replace("A", "A ").split():
            D[symb] += 1
        for _ in range(25 - 1):
            D = get_next_state(D, transition_dict)
        W = sum([len(k) * v for k, v in D.items()])
        ans += int(code[:3]) * W
    return ans


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
