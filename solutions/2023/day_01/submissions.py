lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE

def part1(lines):
    ans = 0
    for line in lines:
        numbers = list(filter(str.isnumeric, line))
        ans += int(numbers[0] + numbers[-1])
    return ans


word2numbers = {
    'one': 'on1e',
    'two': 'tw2o',
    'three': 'th3ree',
    'four': 'fou4r',
    'five': 'fi5ve',
    'six': 'si6x',
    'seven': 'sev7n',
    'eight': 'eig8ht',
    'nine': 'ni9ne'
}


def part2(lines):
    ans = 0
    for line in lines:
        for word, word_num in word2numbers.items():
            line = line.replace(word, word_num)
        numbers = list(filter(str.isnumeric, line))
        ans += int(numbers[0] + numbers[-1])
    return ans

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
print(f'My first answer is {part1(lines)}')

print(f'My answer on test set for the second problem is {part2(test_lines)}')
print(f'My second answer is {part2(lines)}')
