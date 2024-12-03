from aocd import get_data, submit
input = get_data(day=3, year=2024).splitlines()
import re

# WRITE YOUR SOLUTION HERE
def part_1(lines):
    # print(lines)
    cnt = 0
    for exp in lines:
        match = re.findall(r"mul\((\d+),(\d+)\)", exp)
        for (x1, x2) in match:
            cnt += int(x1) * int(x2)
    return cnt

def part_2(lines):
    cnt = 0
    do = True
    for exp in lines:
        exp = exp.replace("don't()", "mul(0,0)").replace("do()", "mul(1,1)")
        match = re.findall(r"mul\((\d+),(\d+)\)", exp)
        for (x1, x2) in match:
            if (x1, x2) == ('0', '0'):
                do = False
                continue
            if (x1, x2) == ('1', '1'):
                do = True
                continue
            if do:
                cnt += int(x1) * int(x2)
    return cnt


# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
