
lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE
def singular_mapping(lines, x):
    for line in lines:
        destination, source, rangE = map(int, line.split())
        if source <= x < source + rangE:
            return destination + x - source
    return x


def mapping(lines, seed):
    x_to_y = []
    for line in lines:
        if line and line[0].isnumeric():
            x_to_y.append(line)
        elif not line:
            seed = singular_mapping(x_to_y, seed)
            x_to_y = []
    if x_to_y:
        seed = singular_mapping(x_to_y, seed)
    return seed

def part_1(lines):
    seeds = map(int, lines[0].split(':')[1].split())
    lines = lines[2:]
    location = [mapping(lines, seed) for seed in seeds]
    return min(location)

def check_mapping(start, end, lines):
    # We check at different location if there is a hole into the mapping return or not
    # If the intertal is clean, f(x) - x should be a constant
    # Otherwise, we need to split it
    ref = mapping(lines, start) - start
    flag = True
    length = 10 # trade-off between speed and precision
    step = (end - start) // length + 1
    for i in range(start, end, step):
        flag = flag & (mapping(lines, i) - i == ref)
    return flag

def part_2(lines):
    seeds = list(map(int, lines[0].split(':')[1].split()))
    intervals = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    flag = False
    while not flag:
        new_intervals = []
        flag = True
        while intervals:
            start, end = intervals.pop()
            if (end - start) >= 2 and not check_mapping(start, end, lines):
                mid = (start + end) // 2
                new_intervals.append((start, mid))
                new_intervals.append((mid, end))
                flag = False
            else:
                new_intervals.append((start, end))
        intervals = new_intervals.copy()
    ans = 1e14
    while intervals:
        start, end = intervals.pop()
        ans = min(ans, mapping(lines, start))
    return ans

test_input = open('input-test.txt').read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line and line[0] == '-':
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f'My answer on test set for the first problem is {part_1(test_lines)}')
print(solution)
print(f'My answer is {part_1(lines)}')

print(f'My answer on test set for the second problem is {part_2(test_lines)}')
print(f'My answer is {part_2(lines)}')
