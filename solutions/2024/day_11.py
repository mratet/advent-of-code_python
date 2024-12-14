from aocd import get_data, submit
input = get_data(day=11, year=2024)
from functools import lru_cache
from math import log
from collections import Counter, defaultdict

# WRITE YOUR SOLUTION HERE
def naive_approach(stones, n):
    assert n < 30
    for _ in range(n):
        new_stones = []
        for i, stone in enumerate(stones):
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                v1, v2 = int(str(stone)[:mid]), int(str(stone)[mid:])
                new_stones.append(v1)
                new_stones.append(v2)
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)

def dict_approach(stones_dict, n):
    stones_dict = Counter(stones_dict)
    for _ in range(n):
        new_stones = defaultdict(int)
        for stone, count in stones_dict.items():
            if stone == 0:
                new_stones[1] += count
                continue
            cnt_bits = int(log(stone, 10)) + 1
            if cnt_bits % 2 == 0:
                middle = 10 ** (cnt_bits // 2)
                new_stones[stone // middle] += count
                new_stones[stone % middle] += count
            else:
                new_stones[stone * 2024] += count
        stones_dict = new_stones.copy()
    return sum(stones_dict.values())

@lru_cache(maxsize=None)
def get_stone_size(stone, i):
    if i == 0:
        return 1
    if stone == 0:
        return get_stone_size(1, i - 1)
    cnt_bits = int(log(stone, 10)) + 1
    if cnt_bits % 2 == 0:
        middle = 10 ** (cnt_bits // 2)
        return get_stone_size(stone // middle, i - 1) + get_stone_size(stone % middle, i - 1)
    else:
        return get_stone_size(stone * 2024, i - 1)

def part_1(lines):
    stones = [int(s) for s in lines.split()]
    # return naive_approach(stones, 25)
    return dict_approach(stones, 25)
    # return sum([get_stone_size(x, 25) for x in stones])

def part_2(lines):
    stones = [int(s) for s in lines.split()]
    return dict_approach(stones, 75)
    # return sum([get_stone_size(x, 75) for x in stones])

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
