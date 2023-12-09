
lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE


def is_zeros(tab):
    for x in tab:
        if x != 0:
            return False
    return True


def part_1(lines):
    ans = 0
    for line in lines:
        oasis = [int(value) for value in line.split()]
        history = [oasis]
        while not is_zeros(oasis):
            ans += oasis[-1]
            prediction = [oasis[i+1] - oasis[i] for i in range(len(oasis)-1)]
            history.append(prediction)
            oasis = prediction
    return ans

def part_2(lines):
    ans = 0
    for line in lines:
        oasis = [int(value) for value in line.split()]
        history = [oasis]
        i = 0
        while not is_zeros(oasis):
            ans += oasis[0] * (-1) ** i
            prediction = [oasis[i+1] - oasis[i] for i in range(len(oasis)-1)]
            history.append(prediction)
            oasis = prediction
            i += 1
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
