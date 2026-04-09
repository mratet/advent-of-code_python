from aocd import get_data

input = get_data(day=6, year=2017)


# WRITE YOUR SOLUTION HERE
def cycle(memory):
    idx = memory.index(max(memory))
    space = memory[idx]
    memory[idx] = 0
    for _ in range(space):
        idx = (idx + 1) % len(memory)
        memory[idx] += 1
    return memory


def simulate_all_cycles(memory):
    seen = {tuple(memory): 0}
    cnt = 0
    memory = cycle(memory)
    while tuple(memory) not in seen:
        cnt += 1
        seen[tuple(memory)] = cnt
        memory = cycle(memory)
    return cnt + 1, seen[tuple(memory)]


def part_1(lines):
    memory = list(map(int, lines.split()))
    cnt, _ = simulate_all_cycles(memory)
    return cnt


def part_2(lines):
    memory = list(map(int, lines.split()))
    cnt, last_seen = simulate_all_cycles(memory)
    return cnt - last_seen


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
