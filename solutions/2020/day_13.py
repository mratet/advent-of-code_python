from aocd import get_data
input = get_data(day=13, year=2020).splitlines()

# WRITE YOUR SOLUTION HERE
def part_1(lines):
    timestamp = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(',') if bus != 'x']
    waiting_time, i = min([(bus - timestamp % bus, i) for i, bus in enumerate(buses)])
    return waiting_time * buses[i]

def part_2(lines):
    pairs = [(int(bus), -i) for i, bus in enumerate(lines[1].split(',')) if bus != 'x']
    nm, am = zip(*pairs)
    return crt(nm, am)

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def crt(nm, am):
    prod = 1
    for n in nm:
        prod *= n

    result = 0
    for i in range(len(nm)):
        prod_i = prod // nm[i]
        _, inv_i, _ = gcd_extended(prod_i, nm[i])
        result += am[i] * prod_i * inv_i

    return result % prod

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
