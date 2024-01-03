import itertools, re

from aocd import get_data
input = get_data(day=15, year=2015).splitlines()

teaspoons = 100
calories_count = 500

def _parse(input):
    ingredients = []
    pattern = r'([-\d]\d*)'
    for line in input:
        matchs = re.findall(pattern, line)
        capacity, durability, flavor, texture, calories = map(int, matchs)
        ingredients.append((capacity, durability, flavor, texture, calories))
    return list(zip(*ingredients))

def dot_product(v1, v2):
    return sum([x * y for x, y in zip(v1, v2)])

def part_1(input):
    ingredients = _parse(input)
    best_score = 0
    for i, j, k in itertools.product(range(teaspoons), range(teaspoons), range(teaspoons)):
        if i + j + k <= teaspoons:
            l = teaspoons - i - j - k
            vect = (i, j, k, l)
            capa_score = dot_product(ingredients[0], vect)
            dura_score = dot_product(ingredients[1], vect)
            flav_score = dot_product(ingredients[2], vect)
            text_score = dot_product(ingredients[3], vect)
            if capa_score < 0 or dura_score < 0 or flav_score < 0 or text_score < 0:
                continue
            best_score = max(best_score, capa_score * dura_score * flav_score * text_score)
    return best_score

def part_2(input):
    ingredients = _parse(input)
    best_score = 0
    for i, j, k in itertools.product(range(teaspoons), range(teaspoons), range(teaspoons)):
        if i + j + k <= teaspoons:
            l = teaspoons - i - j - k
            vect = (i, j, k, l)
            capa_score = dot_product(ingredients[0], vect)
            dura_score = dot_product(ingredients[1], vect)
            flav_score = dot_product(ingredients[2], vect)
            text_score = dot_product(ingredients[3], vect)
            if capa_score < 0 or dura_score < 0 or flav_score < 0 or text_score < 0:
                continue

            calories = dot_product(ingredients[4], vect)
            if calories == calories_count:
                best_score = max(best_score, capa_score * dura_score * flav_score * text_score)

    return best_score

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
