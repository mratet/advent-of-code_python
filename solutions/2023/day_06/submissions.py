
lines = open('input.txt').read().splitlines()

# WRITE YOUR SOLUTION HERE
def nb_records(time, distance):
    """
    The total distance is : D = v * (time - t_charge)
    By definition, v = t_charge (= x)
    We're looking for points s.t x * (time - x) - distance >= 0
    In particular, we're computing the distance between both squares-roots
    With a bit of basic algebra, we can show that :
    """
    nb_records = int((time ** 2 - 4 * distance) ** 0.5)
    return nb_records

def part_1(lines):
    ans = 1
    times = list(map(int, lines[0].split(':')[1].split()))
    distances = list(map(int, lines[1].split(':')[1].split()))
    for i in range(len(times)):
        records = 0
        time, distance = times[i], distances[i]
        for j in range(time):
            distance_bateau = j * (time - j)
            if distance_bateau > distance:
                records += 1
        ans *= records
    return ans

def part_2(lines):
    time = int(lines[0].split(':')[1].replace(' ', ''))
    distance = int(lines[1].split(':')[1].replace(' ', ''))
    return nb_records(time, distance)
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
