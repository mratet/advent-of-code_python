from collections import defaultdict, deque
from itertools import pairwise, product

from aocd import get_data

input = get_data(day=21, year=2024).splitlines()

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


def gen_next_sequence(sequence, mapping):
    seq = "A" + sequence
    return "".join(mapping[s1 + s2] + "A" for s1, s2 in pairwise(seq))


def generate_shortest_paths(start, end):
    start = keypad_to_corr[start]
    end = keypad_to_corr[end]
    if start == end:
        return ["A"]
    forbidden = (3, 0)
    queue = deque([[start]])
    visited = set()
    shortest_paths = []
    min_length = float("inf")
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == end:
            moves = "".join(DIRS[(col2 - col1, row2 - row1)] for (row1, col1), (row2, col2) in pairwise(path))
            if len(moves) < min_length:
                shortest_paths = [moves]
                min_length = len(moves)
            elif len(moves) == min_length:
                shortest_paths.append(moves)
            continue
        if current in visited and len(path) > min_length:
            continue
        visited.add(current)
        row, col = current
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (row + d_row, col + d_col)
            n_row, n_col = neighbor
            if 0 <= n_row < 4 and 0 <= n_col < 3 and neighbor != forbidden and neighbor not in path:
                queue.append([*path, neighbor])
    return shortest_paths


def generate_keypad_mappings(code):
    pairs = list(pairwise("A" + code))
    all_paths = [generate_shortest_paths(start, end) for start, end in pairs]
    keys = [start + end for start, end in pairs]
    return [dict(zip(keys, combo, strict=False)) for combo in product(*all_paths)]


def find_best_keypad_mapping(code, direction):
    keypad_mappings = generate_keypad_mappings(code)

    def score(mapping):
        w = gen_next_sequence(code, mapping)
        for _ in range(5):
            w = gen_next_sequence(w, direction)
        return len(w)

    return min(keypad_mappings, key=score)


def part_1(lines):
    ans = 0
    for code in lines:
        keypad_mapping = find_best_keypad_mapping(code, best_direction)
        w = gen_next_sequence(code, keypad_mapping)
        for _ in range(2):
            w = gen_next_sequence(w, best_direction)
        ans += int(code[:3]) * len(w)
    return ans


def get_transition_dict(direction):
    d = {}
    for v in direction.values():
        seq = "A" + v + "A"
        d[v + "A"] = [direction[m1 + m2] + "A" for m1, m2 in pairwise(seq)]
    d["A"] = ["A"]
    return d


def get_next_state(state, transition_dict):
    new_state = defaultdict(int)
    for k, count in state.items():
        for symb in transition_dict[k]:
            new_state[symb] += count
    return new_state


def part_2(lines):
    transition_dict = get_transition_dict(best_direction)
    ans = 0
    for code in lines:
        keypad_mapping = find_best_keypad_mapping(code, best_direction)
        w = gen_next_sequence(code, keypad_mapping)
        w = gen_next_sequence(w, best_direction)
        state = defaultdict(int)
        for symb in w.replace("A", "A ").split():
            state[symb] += 1
        for _ in range(24):
            state = get_next_state(state, transition_dict)
        ans += int(code[:3]) * sum(len(k) * v for k, v in state.items())
    return ans


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
