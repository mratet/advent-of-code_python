from typing import List
from copy import deepcopy
import re

from aocd import get_data
from dataclasses import dataclass

input = get_data(day=24, year=2018)


@dataclass
class Units:
    type: str
    count: int
    hit_points: int
    attack_damage: int
    attack_type: str
    initiative: int
    weaknesses: List[str]
    immunities: List[str]

    def __hash__(self):
        return hash(
            (
                self.type,
                self.hit_points,
                self.attack_damage,
                self.attack_type,
                self.initiative,
                tuple(sorted(self.weaknesses)),
                tuple(sorted(self.immunities)),
            )
        )

    @property
    def effective_power(self) -> int:
        return self.count * self.attack_damage

    @property
    def is_alive(self) -> bool:
        return self.count > 0

    def compute_damage(self, target) -> int:
        if self.attack_type in target.immunities:
            return 0
        return (
            2 * self.effective_power
            if self.attack_type in target.weaknesses
            else self.effective_power
        )


def parse_army_input(text: str) -> List[Units]:
    groups = []
    current_army = None
    current_lines = []

    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.endswith(":"):
            current_army = line[:-1]
            continue
        # Line continuation
        if re.match(r"^\d+ units each with", line) or current_lines:
            current_lines.append(line)
            if "initiative" in line:
                full_line = " ".join(current_lines)
                groups.append((current_army, full_line))
                current_lines = []

    pattern = re.compile(
        r"(?P<count>\d+) units each with (?P<hp>\d+) hit points(?: \((?P<traits>.*?)\))?"
        r" with an attack that does (?P<dmg>\d+) (?P<dtype>\w+) damage at initiative (?P<init>\d+)"
    )

    units = []
    for army, line in groups:
        match = pattern.match(line)
        if not match:
            raise ValueError(f"Line parsing failed: {line}")

        weaknesses = []
        immunities = []
        traits = match.group("traits")
        if traits:
            for part in traits.split(";"):
                part = part.strip()
                if part.startswith("weak to"):
                    weaknesses = [x.strip() for x in part[8:].split(",")]
                elif part.startswith("immune to"):
                    immunities = [x.strip() for x in part[10:].split(",")]

        units.append(
            Units(
                type=army,
                count=int(match.group("count")),
                hit_points=int(match.group("hp")),
                attack_damage=int(match.group("dmg")),
                attack_type=match.group("dtype"),
                initiative=int(match.group("init")),
                weaknesses=weaknesses,
                immunities=immunities,
            )
        )

    return units


def target_selection(units):
    units = sorted(units, key=lambda u: (u.effective_power, u.initiative), reverse=True)
    units_attacked = []
    attack_dict = {}
    for unit in units:
        op_units = [u for u in units if u.type != unit.type and u not in units_attacked]
        if not op_units:
            continue
        target = max(
            op_units,
            key=lambda u: (unit.compute_damage(u), u.effective_power, u.initiative),
        )
        if unit.compute_damage(target) == 0:
            continue
        attack_dict[unit] = target
        units_attacked.append(target)
    return attack_dict


def attacking_phase(attacking_dict, units_alived):
    full_damage = 0
    units_alived.sort(key=lambda u: u.initiative, reverse=True)
    for unit in units_alived:
        if not unit.is_alive or unit not in attacking_dict:
            continue
        target = attacking_dict[unit]
        damage = unit.compute_damage(target) // target.hit_points
        target.count -= damage
        full_damage += damage
    return full_damage


def battle(armies):
    while True:
        units_alived = [u for u in armies if u.is_alive]
        if len({u.type for u in units_alived}) == 1:
            return units_alived[0].type, sum(u.count for u in units_alived)
        attacking_dict = target_selection(units_alived)
        battle_damages = attacking_phase(attacking_dict, units_alived)
        if battle_damages == 0:
            return "Draw", -1


def set_immune_system_boost(units, boost):
    new_units = deepcopy(units)
    for unit in new_units:
        if unit.type == "Immune System":
            unit.attack_damage += boost
    return new_units


def find_minimum_immune_system_boost(armies):
    l, r = 1, 20000
    while l <= r:
        attack_boost = (l + r) // 2
        new_armies = set_immune_system_boost(armies, attack_boost)
        winning_type, _ = battle(new_armies)
        if winning_type == "Immune System":
            r = attack_boost - 1
        else:
            l = attack_boost + 1
    return l


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    armies = parse_army_input(lines)
    _, remaining_units = battle(armies)
    return remaining_units


def part_2(lines):
    armies = parse_army_input(lines)
    min_boost = find_minimum_immune_system_boost(armies)
    armies = set_immune_system_boost(armies, min_boost)
    _, remaining_units = battle(armies)
    return remaining_units


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
