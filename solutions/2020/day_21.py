import re
from functools import reduce

from aocd import get_data

input = get_data(day=21, year=2020)


# WRITE YOUR SOLUTION HERE
def parse_recipe(data):
    pattern = r"([\w\s]+) \(contains ([\w\s,]+)\)"
    recipes = []
    allergens = set()

    for match in re.finditer(pattern, data):
        ingredients = match.group(1).split()
        recipe_allergens = [a.strip() for a in match.group(2).split(",")]
        recipes.append({"ingredients": ingredients, "allergens": recipe_allergens})
        allergens.update(recipe_allergens)
    return recipes, allergens


def get_candidates(recipes, allergens):
    candidates = {}
    for allergen in allergens:
        ingredient_sets = [set(r["ingredients"]) for r in recipes if allergen in r["allergens"]]
        candidates[allergen] = reduce(set.intersection, ingredient_sets)
    return candidates


def get_mapping(candidates):
    mapping = {}
    while candidates:
        allergen, (ingredient,) = next((a, s) for a, s in candidates.items() if len(s) == 1)
        mapping[allergen] = ingredient
        candidates = {a: s - {ingredient} for a, s in candidates.items() if a != allergen}
    return mapping


def part_1(lines):
    recipes, allergens = parse_recipe(lines)
    mapping = get_mapping(get_candidates(recipes, allergens))
    return sum(len(set(recipe["ingredients"]) - set(mapping.values())) for recipe in recipes)


def part_2(lines):
    recipes, allergens = parse_recipe(lines)
    mapping = dict(sorted(get_mapping(get_candidates(recipes, allergens)).items()))
    return ",".join(mapping.values())


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
