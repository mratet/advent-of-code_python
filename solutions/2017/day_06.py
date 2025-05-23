from aocd import get_data, submit

input = get_data(day=6, year=2017)


# WRITE YOUR SOLUTION HERE
def cycle(memory):
    idx = memory.index(max(memory))
    space = memory[idx]
    memory[idx] = 0
    while space:
        memory[(idx + 1) % len(memory)] += 1
        idx += 1
        space -= 1
    return memory


def simulate_all_cycles(memory):
    seen = {tuple(memory): 0}
    cnt = 1
    while True:
        next_memory = cycle(memory)
        if tuple(next_memory) in seen:
            break
        seen[tuple(next_memory)] = cnt
        cnt += 1
        memory = next_memory
    return cnt, seen[tuple(next_memory)]


def part_1(lines):
    memory = [int(n) for n in lines.split()]
    cnt, _ = simulate_all_cycles(memory)
    return cnt


def part_2(lines):
    memory = [int(n) for n in lines.split()]
    cnt, last_seen = simulate_all_cycles(memory)
    return cnt - last_seen


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
