import itertools, re, collections
from aocd import get_data
input = get_data(day=21, year=2016).splitlines()

def scrambling(instructions, password, reverse=False):
    password = list(password)
    if reverse:
        instructions = instructions[::-1]

    # Hard-coded because it don't seem relevant to code a general formulation
    position_shift = [1, 1, 6, 2, 7, 3, 0, 4] if reverse else [7, 6, 5, 4, 2, 1, 0, 7]

    for line in instructions:
        instrc = line.split()

        match instrc[0]:
            case 'swap':
                X, Y = instrc[2], instrc[-1]
                if instrc[1] == 'position':
                    X, Y = int(X), int(Y)
                    password[X], password[Y] = password[Y], password[X]
                else:
                    i, j = password.index(X), password.index(Y)
                    password[i], password[j] = password[j], password[i]

            case 'rotate':
                if instrc[1] == 'based':
                    n = password.index(instrc[-1])
                    X = position_shift[n]
                else:
                    n = 1 if instrc[1] == 'left' else -1
                    if reverse: n *= -1
                    X = n * int(instrc[2])
                password = password[X:] + password[:X]

            case 'reverse':
                X, Y = int(instrc[2]), int(instrc[-1])
                password = password[:X] + password[X: Y + 1][::-1] + password[Y + 1:]

            case 'move':
                X, Y = int(instrc[2]), int(instrc[-1])
                if reverse: X, Y = Y, X
                c = password.pop(X)
                password = password[:Y] + [c] + password[Y:]

    return ''.join(password)


def part_1(input):
    password = 'abcdefgh'
    return scrambling(input, password)

def part_2(input):
    reverse_pass = 'fbgdceah'
    return scrambling(input, reverse_pass, reverse=True)

print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
