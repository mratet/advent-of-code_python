from aocd import get_data
input = get_data(day=2, year=2015).splitlines()

def area(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * l * h + min(w*l, w*h, l*h)

def ribbon_area(l, w, h):
    a, b, _ = sorted([l, w, h])
    return l * w * h + 2 * a + 2 * b

def part_1(input):
    t = 0
    for line in input:
        l, w, h = list(map(int, line.split('x')))
        t += area(l, w, h)
    return t

def part_2(input):
    t = 0
    for line in input:
        l, w, h = list(map(int, line.split('x')))
        t += ribbon_area(l, w, h)
    return t

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
