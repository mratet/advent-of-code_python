import re, math
lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE
def part_1(lines):
    binary = {'L': 0, 'R': 1}
    movements = [binary[c] for c in lines[0]]
    network = {}
    for line in lines[2:]:
        source, target_l, target_r = re.findall(r'\b[A-Z]{3}\b', line)
        network[source] = (target_l, target_r)

    i = 0
    state = 'AAA'
    while True:
        state = network[state][movements[i % len(movements)]]
        if state == "ZZZ":
            return i + 1
        i += 1

def part_2(lines):
    binary = {'L': 0, 'R': 1}
    movements = [binary[c] for c in lines[0]]
    network = {}
    for line in lines[2:]:
        source, target_l, target_r = re.findall(r'\b[A-Z]{3}\b', line)
        network[source] = (target_l, target_r)

    starting_states = [source for source in network.keys() if source[2] == 'A']
    tab = []
    for starting_state in starting_states:
        i = 0
        state = starting_state
        while True:
            state = network[state][movements[i % len(movements)]]
            if state[2] == "Z":
                tab.append(i + 1)
                break
            i += 1

    lcm_result = tab[0]

    for number in tab[1:]:
        lcm_result = abs(lcm_result * number) // math.gcd(lcm_result, number)

    return lcm_result

# END OF SOLUTION


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
