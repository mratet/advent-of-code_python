from aocd import get_data, submit
input = get_data(day=11, year=2024)
from functools import lru_cache

# WRITE YOUR SOLUTION HERE
def get_next_state(stones):
    ### Naive approach
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == 0:
            new_stones.append(1)
        elif len(str(stones[i])) % 2 == 0:
            idx =len(str(stones[i])) // 2
            val1, val2 = str(stones[i])[:idx], str(stones[i])[idx:]
            new_stones.append(int(val1))
            new_stones.append(int(val2))
        else:
            new_stones.append(stones[i] * 2024)
    return new_stones

def part_1(lines):
    stones = [int(n) for n in lines.split()]
    for _ in range(25):
        stones = get_next_state(stones)
    return len(stones)

@lru_cache(maxsize=None)
def get_stone_size(stone, i):
    if i == 75:
        return 1
    if stone == '0':
        return get_stone_size('1', i + 1)
    elif len(stone) % 2 == 0:
        idx = len(stone) // 2
        return get_stone_size(stone[:idx], i + 1) + get_stone_size(str(int(stone[idx:])), i + 1)
    else:
        return get_stone_size(str(int(stone) * 2024), i + 1)

def part_2(lines):
    stones = [s for s in lines.split()]
    return sum([get_stone_size(x, 0) for x in stones])

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
