from aocd import get_data
input = get_data(day=10, year=2015)

def next_step(sequence):
    current_c, count = sequence[0], 1
    next_sequence = ""
    for c in sequence[1:]:
        if c == current_c:
            count += 1
        else:
            next_sequence += str(count) + current_c
            current_c, count = c, 1
    next_sequence += str(count) + current_c

    return next_sequence

def part_1(input):
    step = 40
    for _ in range(step):
        input = next_step(input)
    return len(input)

def part_2(input):
    step = 50
    for _ in range(step):
        input = next_step(input)
    return len(input)

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
