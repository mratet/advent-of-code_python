import itertools
import re
from collections import defaultdict, deque

from aocd import get_data

input = get_data(day=11, year=2016).splitlines()


def _parse_input(input_lines):
    pair_locations = defaultdict(dict)
    component_regex = re.compile(r"(\w+)(?:-compatible)? (generator|microchip)")

    for i, line in enumerate(input_lines):
        for element, type in component_regex.findall(line):
            comp_name = element[0].upper() + element[1]
            comp_type = type[0].upper()
            pair_locations[comp_name][comp_type] = i

    return sorted([(loc["G"], loc["M"]) for loc in pair_locations.values()])


def will_explode(pairs):
    for pair in pairs:
        g_floor, c_floor = pair
        if g_floor != c_floor and any(gf == c_floor for (gf, _) in pairs):
            return True
    return False


def bfs(pairs):
    queue = deque([(0, pairs, 0)])
    seen = {(0, pairs)}

    while queue:
        curr_elevator_pos, pairs, steps = queue.popleft()

        if all(pair == (3, 3) for pair in pairs):
            return steps

        items_on_current_floor = []
        for idx, (g_floor, c_floor) in enumerate(pairs):
            if g_floor == curr_elevator_pos:
                items_on_current_floor.append((idx, "G"))
            if c_floor == curr_elevator_pos:
                items_on_current_floor.append((idx, "M"))

        for next_elevator_pos in (curr_elevator_pos - 1, curr_elevator_pos + 1):
            if not (0 <= next_elevator_pos <= 3):
                continue

            for num_items_to_move in [1, 2]:
                if len(items_on_current_floor) < num_items_to_move:
                    continue

                for items_to_move in itertools.combinations(items_on_current_floor, num_items_to_move):
                    next_pairs = list(pairs)

                    for pair_idx, item_type in items_to_move:
                        g_floor, c_floor = next_pairs[pair_idx]
                        next_pairs[pair_idx] = (
                            (next_elevator_pos, c_floor) if item_type == "G" else (g_floor, next_elevator_pos)
                        )

                    next_pairs.sort()
                    next_pairs_tuple = tuple(next_pairs)

                    if will_explode(next_pairs_tuple):
                        continue

                    new_state = (next_elevator_pos, next_pairs_tuple)
                    if new_state in seen:
                        continue

                    seen.add(new_state)
                    queue.append((next_elevator_pos, next_pairs_tuple, steps + 1))


def part_1(input):
    pairs = _parse_input(input)
    return bfs(tuple(pairs))


def part_2(input):
    pairs = _parse_input(input)
    return bfs(((0, 0), (0, 0), *pairs))


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
