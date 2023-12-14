import re
lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE
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

def matrixflip(m,d):
    tempm = m.copy()
    if d == 'h':
        for i in range(0, len(tempm), 1):
                tempm[i] = tempm[i][::-1]
    elif d == 'v':
        tempm = tempm[::-1]
    return(tempm)

def left_rotation(entry_platform, n):
    platform = entry_platform.copy()
    for _ in range(n):
        platform = matrixflip(platform, 'h')
        platform = [[row[i] for row in platform] for i in range(len(platform[0]))]
    return platform

def shift(entry_platform, direction):
    platform = entry_platform.copy()
    if direction == 'w':
        return west_shift(platform)
    elif direction == 'n':
        platform = left_rotation(platform, 1)
        platform = west_shift(platform)
        return left_rotation(platform, 3)
    elif direction == 'e':
        platform = left_rotation(platform, 2)
        platform = west_shift(platform)
        return left_rotation(platform, 2)
    elif direction == 's':
        platform = left_rotation(platform, 3)
        platform = west_shift(platform)
        return left_rotation(platform, 1)


def compute_load(platform):
    load = 0
    platform = left_rotation(platform.copy(), 1)
    for line in platform:
        load += sum([1 + i for i, c in enumerate(line[::-1]) if c == 'O'])

    return load

def part_1(lines):
    platform = shift(lines, 'n')
    ans = compute_load(platform)

    return ans

def part_2(lines):
    platform = lines.copy()
    sequences = ''
    for _ in range(400):
        for c in 'nwse':
            platform = shift(platform, c)
        sequences += str(compute_load(platform)) + ' '

    regex = re.compile(r'(.+ .+)( \1)+')
    match = regex.search(sequences)
    cycle = match.group(1)
    length_cycle = cycle.count(' ') + 1
    len_numbers = len(str(compute_load(platform)) + ' ')
    start_cycle = match.start() // len_numbers - 1

    nb_cycles = 1e9
    ans = sequences.split()[int((nb_cycles - start_cycle) % length_cycle)]
    return ans


# END OF SOLUTION


test_input = open('input-test.txt').read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == '-':
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f'My answer on test set for the first problem is {part_1(test_lines)}')
print(solution)
print(f'My answer is {part_1(lines)}')

print(f'My answer on test set for the second problem is {part_2(test_lines)}')
print(f'My answer is {part_2(lines)}')
