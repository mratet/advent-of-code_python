from aocd import get_data
input = get_data(day=14, year=2020).splitlines()
import re

# WRITE YOUR SOLUTION HERE
def solve(input, part):
    memory = {}
    bitmask = None
    for line in input:
        if line[:3] == 'mem':
            idx, val = re.search(r"mem\[(\d+)\] = (\d+)", line).groups()
            if part == 'part_1':
                binary_val = ['1' if val == '1' else '0' for val in format(int(val), '36b')]
                next_val = [mask_val if mask_val != 'X' else bin_val for (mask_val, bin_val) in zip(bitmask, binary_val)]
                memory[idx] = int(''.join(next_val), 2)
            elif part == 'part_2':
                binary_idx = ['1' if val == '1' else '0' for val in format(int(idx), '36b')]
                next_val = [mask_val if mask_val != '0' else bin_val for (mask_val, bin_val) in zip(bitmask, binary_idx)]
                quant_val = ''.join(next_val)
                n = quant_val.count('X')
                for i in range(2 ** n):
                    next_quant = quant_val
                    bits = ['1' if val == '1' else '0' for val in format(i, f'{str(n)}b')]
                    for bit in bits:
                        next_quant = next_quant.replace('X', bit, 1)
                    memory[int(next_quant, 2)] = int(val)
        else:
            bitmask = list(line[7:])
    return sum([val for val in memory.values()])

def part_1(lines):
    return solve(lines, 'part_1')

def part_2(lines):
    return solve(lines, 'part_2')

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
