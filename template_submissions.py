
lines = open('input.txt').read().split("\n")[:-1]

# WRITE YOUR SOLUTION HERE
def part1(lines):
    return 0

def part2(lines):
    return 0
# END OF SOLUTION


test_input = open('input-test.txt').read().split("\n")
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == '-':
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f'My answer on test set for the first problem is {part1(test_lines)}')
print(solution)
print(f'My answer is {part1(lines)}')

print(f'My answer on test set for the second problem is {part2(test_lines)}')
print(f'My answer is {part2(lines)}')
