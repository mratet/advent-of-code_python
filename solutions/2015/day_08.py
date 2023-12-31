from aocd import get_data
input = get_data(day=8, year=2015).splitlines()

def part_1(input):
    return sum(len(s) - len(eval(s)) for s in input)

def part_2(input):
    return sum(s.count("\\") + s.count('"') + 2 for s in input)

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
