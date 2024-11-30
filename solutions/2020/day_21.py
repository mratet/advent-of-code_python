from aocd import get_data
input = get_data(day=21, year=2020)
import re

# WRITE YOUR SOLUTION HERE
def parse_recipe(input):
    pattern = r"([\w\s]+) \(contains ([\w\s,]+)\)"
    recipes = []
    ings = set()
    alls = set()

    for match in re.finditer(pattern, input):
        ingredients = match.group(1).split()
        allergens = [a.strip() for a in match.group(2).split(',')]  
        recipes.append({"ingredients": ingredients, "allergens": allergens})
        for ing in ingredients:
            ings.add(ing)
        for all in allergens:
            alls.add(all)
    return recipes, ings, alls

def get_next_dict(candidates, true_name, encode_name):
    new_candidates = {}
    for name, t in candidates.items():
        if name != true_name:
            new_candidates[name] = [v for v in t if v != encode_name]
    return new_candidates

def get_candidates(recipes, allergens):
    candidates = {}
    for allergen in allergens:
        S = set()
        for recipe in recipes:
            if allergen in recipe["allergens"]:
                if not S:
                    S = set(recipe["ingredients"])
                else:
                    S = S.intersection(recipe["ingredients"])
        candidates[allergen] = S
    return candidates

def get_mapping_dict(candidates):
    mapping = {}
    while candidates:
        for ingredient, names in candidates.items():
            if len(names) == 1:
                (name,) = names
                mapping[ingredient] = name
                candidates = get_next_dict(candidates, ingredient, name)
    return mapping

def part_1(lines):
    recipes, ingredients, allergens = parse_recipe(lines)
    candidates = get_candidates(recipes, allergens)
    mapping = get_mapping_dict(candidates)
    return sum([len(set(recipe['ingredients']) - set(mapping.values())) for recipe in recipes])

def part_2(lines):
    recipes, ingredients, allergens = parse_recipe(lines)
    candidates = get_candidates(recipes, allergens)
    mapping = dict(sorted(get_mapping_dict(candidates).items()))
    return ','.join(mapping.values())

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

