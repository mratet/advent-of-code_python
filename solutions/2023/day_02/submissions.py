
lines = open('input.txt', 'r').readlines()

# WRITE YOUR SOLUTION HERE


def main(lines):

    m_values = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    ans = 0
    for id, line in enumerate(lines):
        games = line.split(':')[1][:-1].split(';')
        values = m_values.copy()
        for game_set in games:
            game = game_set.split(',')
            for tirage in game:
                tirage = tirage.split(' ')
                number, color = tirage[1], tirage[2]
                values[color] = max(int(number), values[color])
        ans += values['green'] * values['red'] * values['blue']

    return ans
# END OF SOLUTION

test_input = open('input-test.txt').readlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line[0] == '-':
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f'My answer on test set is {main(test_lines)}')
print(solution)
print(f'My answer is {main(lines)}')
