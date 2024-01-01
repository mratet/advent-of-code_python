from aocd import get_data
input = get_data(day=12, year=2015)

import re, json

def part_1(input):
    matchs = re.findall(r'([-\d]\d*)', input)
    return sum([int(match) for match in matchs])

def recsum(r):
    s = 0

    if isinstance(r, list):
        d = r
    elif isinstance(r, dict):
        if 'red' in r.values():
            return 0
        else:
            d = r.values()
    else:
        return 0

    for v in d:
        try:
            s += v
        except:
            s += recsum(v)

    return s

def part_2(input):
    d = json.loads(input)
    return recsum(d)


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

