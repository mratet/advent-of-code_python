from aocd import get_data

input = get_data(day=8, year=2020).splitlines()
from typing import List


# WRITE YOUR SOLUTION HERE
def compute_accumulator(lines: List[str]) -> int:
    i = 0
    hist = {0}
    accumulator = 0
    candidates = []
    terminated = True
    while i < len(lines):
        intruct, number = lines[i][:3], int(lines[i][4:])
        match intruct:
            case "acc":
                accumulator += number
                i += 1
            case "jmp":
                candidates.append((i, lines[i]))
                i += number
            case "nop":
                candidates.append((i, lines[i]))
                i += 1
        if i in hist:
            terminated = False
            break
        hist.add(i)
    return accumulator, candidates, terminated


def part_1(lines):
    acc, candidates, terminated = compute_accumulator(lines)
    return acc


def part_2(lines):
    _, candidates, _ = compute_accumulator(lines)
    for i, line in candidates:
        new_lines = lines[:]
        op = "nop" if line[:3] == "jmp" else "jmp"
        new_lines[i] = op + line[3:]
        acc, _, terminated = compute_accumulator(new_lines)
        if terminated:
            return acc


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
