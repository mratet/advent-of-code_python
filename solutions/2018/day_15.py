from aocd import get_data
from copy import deepcopy
from collections import deque
from dataclasses import dataclass, field

input = get_data(day=15, year=2018).splitlines()

READING_ORDER = lambda p: (p[1], p[0])


def find_closest(start, targets, blocked_case):
    to_visit = deque([start])
    distances = {start: 0}
    reachable_targets = []

    while to_visit:
        for _ in range(len(to_visit)):
            node = to_visit.popleft()
            if node in targets:
                reachable_targets.append(node)

            x, y = node
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (x + dx, y + dy)
                if neighbor not in blocked_case and neighbor not in distances:
                    distances[neighbor] = distances[node] + 1
                    to_visit.append(neighbor)

        if reachable_targets:
            return reachable_targets

    return reachable_targets


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


@dataclass(order=True)
class Unit:
    sort_index: tuple = field(init=False, repr=False)
    x: int
    y: int
    type: str
    attack_power: int = 3
    hit_points: int = 200
    is_alive: bool = True

    @property
    def position(self):
        return (self.x, self.y)

    def __post_init__(self):
        self.update_sort_index()

    def update_sort_index(self):
        self.sort_index = (self.y, self.x)

    def move(self, targets_range, blocked_case):
        nearest_cases = find_closest(self.position, targets_range, blocked_case)

        if not nearest_cases:
            return

        destination = min(nearest_cases, key=READING_ORDER)
        available_neighbors = find_closest(
            destination,
            [n for n in self.get_neighbors() if n not in blocked_case],
            blocked_case,
        )
        self.x, self.y = min(available_neighbors, key=READING_ORDER)
        self.update_sort_index()

    def attack(self, targets):
        targets_in_range = [t for t in targets if t.position in self.get_neighbors()]

        if not targets_in_range:
            return

        unit_attacked = min(
            targets_in_range, key=lambda unit: (unit.hit_points, unit.y, unit.x)
        )
        unit_attacked.hit_points -= self.attack_power
        if unit_attacked.hit_points <= 0:
            unit_attacked.is_alive = False

    def adjacent_target(self, targets):
        return any(t.position in self.get_neighbors() for t in targets)

    def get_neighbors(self):
        return [
            (self.x - 1, self.y),
            (self.x + 1, self.y),
            (self.x, self.y - 1),
            (self.x, self.y + 1),
        ]


def parse_input(lines):
    walls = []
    units = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                walls.append((x, y))
            elif c in "GE":
                units.append(Unit(x, y, c))

    return walls, units


def simulate(walls, units, part="part_1"):
    round = 0
    while True:
        units.sort()

        if part == "part_2" and any(
            not unit.is_alive and unit.type == "E" for unit in units
        ):
            return -1

        for unit in units:
            if not unit.is_alive:
                continue

            blocked_cases = walls + [(u.x, u.y) for u in units if u.is_alive]
            targets = [u for u in units if u.is_alive and u.type != unit.type]
            if not targets:
                allies_hp = [
                    u.hit_points for u in units if u.is_alive and u.type == unit.type
                ]
                return round * sum(allies_hp)

            if not unit.adjacent_target(targets):
                targets_range = [
                    neigh
                    for target in targets
                    for neigh in target.get_neighbors()
                    if neigh not in blocked_cases
                ]
                if not targets_range:
                    continue
                unit.move(targets_range, blocked_cases)

            unit.attack(targets)

        round += 1


def set_elves_attack_power(units, power):
    new_units = deepcopy(units)
    for unit in new_units:
        if unit.type == "E":
            unit.attack_power = power
    return new_units


def find_minimum_elves_power(walls, units):
    l, r = 4, 200
    while l <= r:
        elves_power = (l + r) // 2
        new_units = set_elves_attack_power(units, elves_power)
        outcome = simulate(walls, new_units, part="part_2")
        if outcome > 0:
            r = elves_power - 1
        else:
            l = elves_power + 1
    return l


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    walls, units = parse_input(lines)
    return simulate(walls, units)


def part_2(lines):
    walls, units = parse_input(lines)
    min_power = find_minimum_elves_power(walls, units)
    final_units = set_elves_attack_power(units, min_power)
    return simulate(walls, final_units, part="part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
