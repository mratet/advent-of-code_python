import itertools, re, collections
from aocd import get_data
input = get_data(day=4, year=2016).splitlines()

def cipher(letters, n):
    phrase = []
    for c in letters:
        if c.isalpha():
            c = chr((ord(c) - ord('a') + int(n)) % 26 + ord('a'))
        phrase.append(c)
    return ''.join(phrase)

def solve(input, part='part_1'):
    t = 0
    for line in input:
        *letters, password = line.split('-')
        ID, checksum = password.split('[')

        count = collections.Counter(''.join(letters))
        sorted_count = sorted(count.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
        most_freq_letters = ''.join([x for (x, y) in sorted_count])
        if most_freq_letters.startswith(checksum[:-1]):
            t += int(ID)
            if 'north' in cipher(' '.join(letters), int(ID)) and part == 'part_2':
                return ID
    return t

def part_1(input):
    return solve(input)

def part_2(input):
    return solve(input, part='part_2')

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
