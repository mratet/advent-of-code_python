from collections import defaultdict

from math import ceil
from aocd import get_data

aoc_input = get_data(day=14, year=2019).splitlines()

TRILLION = 1000000000000


def _parse_input(lines):
    reactions = {}
    for line in lines:
        inputs_str, output_str = line.split(" => ")
        output_amount, output_chem = output_str.split()
        ingredients = []
        for item in inputs_str.split(", "):
            amount, chem = item.split()
            ingredients.append((chem, int(amount)))
        reactions[output_chem] = (int(output_amount), ingredients)
    return reactions


# Topological sort
def get_reaction_order(reactions):
    order = []
    visited = set()

    def visit(chemical):
        if chemical == "ORE":
            return
        if chemical in visited:
            return
        visited.add(chemical)
        _, ingredients = reactions[chemical]
        for ingredient_name, _ in ingredients:
            visit(ingredient_name)
        order.append(chemical)

    visit("FUEL")
    return order[::-1]


def solve(reaction_order, reactions, fuel_needed=1):
    chemicals_needed = defaultdict(int)
    chemicals_needed["FUEL"] = fuel_needed
    for chemical in reaction_order:
        output_amount, ingredients = reactions[chemical]
        reaction_count = ceil(chemicals_needed[chemical] / output_amount)
        for chem, amount in ingredients:
            chemicals_needed[chem] += amount * reaction_count
    return chemicals_needed["ORE"]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    reactions = _parse_input(lines)
    reaction_order = get_reaction_order(reactions)
    return solve(reaction_order, reactions)


def part_2(lines):
    reactions = _parse_input(lines)
    reaction_order = get_reaction_order(reactions)

    l, r = 1, TRILLION
    while l <= r:
        fuel = (l + r) // 2
        ore_needed = solve(reaction_order, reactions, fuel)
        if ore_needed < TRILLION:
            l = fuel + 1
        else:
            r = fuel - 1
    return r


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
