import itertools, re, collections, math
from aocd import get_data
input = int(get_data(day=19, year=2016))

def recursive_part_1(N):
    elfs = list(range(1, N + 1))
    while len(elfs) > 1:
        n = len(elfs)
        for i in range(1, n + 1, 2):
            elfs[i % n] = 0
        elfs = [elt for elt in elfs if elt != 0]
    return elfs[0]

def recursive_part_2(tab):
    # Used to print first 100 values to find a pattern
    # Possible to use two deque 'left' and 'right' to design an iterative solution
    n = len(tab)
    if n == 1 or n == 2:
        return tab[0]
    if n % 2 == 1:
        tab.pop(n // 2)
    else:
        tab.pop(n // 2 + 1)
    return recursive_part_2(tab[1:] + tab[:1])


def part_2(N):
    # largest power of 3 smaller than N
    n = 3 ** int(math.log(N, 3))
    return N - n + max(N - 2 * n, 0) if N != n else n


def part_1(N):
    # largest power of 2 smaller than N
    n = 2 ** int(math.log(N, 2))
    return 1 + 2 * (N - n)


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
