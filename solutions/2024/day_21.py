from collections import defaultdict
from itertools import product

from aocd import get_data, submit
input = get_data(day=21, year=2024)
from collections import deque

# WRITE YOUR SOLUTION HERE
direction_keypad = '.^A\n<v>'
DIRS = {'>': (0, 1), '<': (0, -1), 'v': (-1, 0), '^': (1, 0)}
direction_mapping = {
    'AA': 'A',
    'A^': '<',
    'A>': 'v',
    'Av': 'v<', #
    'A<': 'v<<',
    '^^': 'A',
    '^A': '>',
    '^v': 'v',
    '^>': 'v>', #
    '^<': 'v<',
    '>>': 'A',
    '>A': '^',
    '>v': '<',
    '><': '<<',
    '>^': '^<', #
    'vv': 'A',
    'vA': '^>', #
    'v^': '^',
    'v>': '>',
    'v<': '<',
    '<<': 'A',
    '<A': '>>^',
    '<v': '>',
    '<>': '>>',
    '<^': '>^'
}
def solve(sequence, mapping):
    sequence = 'A' + sequence
    seq = []
    for s1, s2 in zip(sequence, sequence[1:]):
        seq.append(mapping[s1 + s2])
        if s1 != s2:
            seq.append('A')
    return ''.join(seq)

def generate_keypad_directions(keypad):
    # Diviser le pavé numérique en lignes
    rows = keypad.split("\n")

    positions = {}
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            positions[char] = (x, y)
    directions = {
        (0, 1): 'v',
        (1, 0): '>',
        (0, -1): '^',
        (-1, 0): '<',
    }
    priority = {'v': 0, '>':1, '^': 2, '<': 3}

    sequences = {}
    for start_char, start_pos in positions.items():
        if start_char == '.': continue

        for end_char, end_pos in positions.items():
            if end_char == '.': continue

            if start_char == end_char:
                sequences[start_char + end_char] = 'A'  #
            else:
                queue = deque([(start_pos, "" )])
                visited = set()

                while queue:
                    current_pos, current_sequence = queue.popleft()

                    if current_pos == end_pos:
                        sequences[start_char + end_char] = ''.join(sorted(current_sequence, key=lambda x: priority[x]))
                        break

                    if current_pos in visited: continue

                    visited.add(current_pos)
                    for (dx, dy), direction in directions.items():
                        next_pos = (current_pos[0] + dx, current_pos[1] + dy)

                        if next_pos in positions.values() and next_pos != positions['.'] and next_pos not in visited:
                            queue.append((next_pos, current_sequence + direction))

    return sequences

# 151826 82 / 70 / 62 / 78 / 60
input2 = """159A
375A
613A
894A
080A"""

# 126384 68 / 60 / 68 / 64 / 64
input3 = """029A
980A
179A
456A
379A"""

def part_1(lines):
    lines = lines.splitlines()
    keypad_mapping = generate_keypad_directions('789\n456\n123\n.0A')
    print(keypad_mapping['19'])

    keypad_mapping['37'] = '<<^^'
    keypad_mapping['A8'] = '<^^^'
    keypad_mapping['61'] = '<<v'
    keypad_mapping['94'] = '<<v'
    keypad_mapping['10'] = '>v'
    keypad_mapping['1A'] = '>>v'
    keypad_mapping['40'] = '>vv'
    keypad_mapping['4A'] = '>>vv'
    keypad_mapping['70'] = '>vvv'
    keypad_mapping['7A'] = '>>vvv'
    keypad_mapping['19'] = '^^>>'

    ans = 0
    for line in lines:
        numeric_part = int(line[:3])
        w1 = solve(line, keypad_mapping)
        # print(w1)
        w2 = solve(w1, direction_mapping)
        # print(w2)
        w3 = solve(w2, direction_mapping)
        # print(w3)
        print(line, len(w3))
        ans += numeric_part * len(w3)
    assert ans != 158110 # Mauvais reponse pour mon input
    return ans

def part_2(lines):
    return
# END OF SOLUTION
print(f'My answer is {part_1(input2)}')
print(f'My answer is {part_1(input3)}')
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
