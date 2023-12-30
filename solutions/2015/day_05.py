from aocd import get_data
input = get_data(day=5, year=2015).splitlines()

import collections

def nice_string_part1(str):
    n = len(str)
    vowels = 'aeiou'
    vowels_count = int(str[0] in vowels)
    forbidden = ['ab', 'cd', 'pq', 'xy']
    double_flag = False

    for i in range(n - 1):
        c1, c2 = str[i], str[i + 1]
        if c2 in vowels:
            vowels_count += 1

        if c1 == c2:
            double_flag = True

        if c1 + c2 in forbidden:
            return False

    return double_flag & (vowels_count >= 3)

def nice_string_part2(str):
    n = len(str)
    double = collections.defaultdict(list)
    letter_repeat = False
    for i in range(n - 2):
        if str[i] == str[i + 2]:
            letter_repeat = True
        double[str[i] + str[i + 1]].append(i)
    double[str[n - 2] + str[n - 1]].append(n - 2)

    double_flag = False
    for tab in double.values():
        if len(tab) > 1 and tab[-1] - tab[0] > 1:
            double_flag = True

    return double_flag and letter_repeat


def part_1(input):
    return sum([nice_string_part1(str) for str in input])


def part_2(input):
    return sum([nice_string_part2(str) for str in input])

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
