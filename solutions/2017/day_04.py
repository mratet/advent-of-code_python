from aocd import get_data, submit
input = get_data(day=4, year=2017).splitlines()
# WRITE YOUR SOLUTION HERE
def part_1(lines):
    ans = 0
    for line in lines:
        words = line.split()
        if len(words) == len(set(words)):
            ans += 1
    return ans

def part_2(lines):
    ans = 0
    for line in lines:
        words = [''.join(sorted(w)) for w in line.split()]
        if len(words) == len(set(words)):
            ans += 1
    return ans
# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

