from aocd import get_data
input = get_data(day=1, year=2015)

def part_1(input):
    t = 0
    for c in input:
        if c == '(':
            t += 1
        else:
            t -=1
    return t

def part_2(input):
    t, i = 0, 0

    while t != -1:
        match input[i]:
            case '(':
                t += 1
            case ')':
                t -=1
        i += 1

    return i

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
