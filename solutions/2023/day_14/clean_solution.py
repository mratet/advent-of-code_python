from aocd import get_data
input = get_data(day=14, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE

def right_rotation(matrix, n):
    for _ in range(n):
        matrix = list(zip(*matrix[::-1]))
    return matrix

def west_shift(platform):
    shifted_platform = []
    for line in platform:
        new_line = list(line)
        position = 0
        for i, c in enumerate(line):
            if c == 'O':
                new_line[position] = 'O'
                if position != i:
                    new_line[i] = '.'
                position += 1
            elif c == '#':
                position = i + 1

        shifted_platform.append(''.join(new_line))
    return shifted_platform

def shift(entry_platform, direction):
    platform = entry_platform.copy()
    if direction == 'w':
        return west_shift(platform)
    elif direction == 'n':
        platform = right_rotation(platform, 3)
        platform = west_shift(platform)
        return right_rotation(platform, 1)
    elif direction == 'e':
        platform = right_rotation(platform, 2)
        platform = west_shift(platform)
        return right_rotation(platform, 2)
    elif direction == 's':
        platform = right_rotation(platform, 1)
        platform = west_shift(platform)
        return right_rotation(platform, 3)

def compute_load(platform):
    load = 0
    platform = right_rotation(platform.copy(), 3)
    for line in platform:
        load += sum([1 + i for i, c in enumerate(line[::-1]) if c == 'O'])

    return load
def part_1(input):
    platform = shift(input, 'n')
    ans = compute_load(platform)

    return ans

def detect_cycle(sequence):
    # Each element has to be different
    visited = set()
    for i, val in enumerate(sequence):
        if val in visited:
            start_cycle = sequence.index(val)
            length_cycle = i - start_cycle
            return start_cycle, length_cycle
        visited.add(val)
    return 0


def part_2(lines):
    platform = lines.copy()
    sequences, loads = [], []

    for _ in range(200):
        sequences.append(hash(tuple(platform)))
        loads.append(compute_load(platform))
        for c in 'nwse':
            platform = shift(platform, c)

    start_cycle, length_cycle = detect_cycle(sequences)
    nb_cycles = 1e9
    ans = loads[start_cycle + int((nb_cycles - start_cycle) % length_cycle)]

    return ans
# END OF SOLUTION


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
