from aocd import get_data, submit
input = get_data(day=7, year=2024).splitlines()

# WRITE YOUR SOLUTION HERE
def convert_base(number, base, length):
    if number == 0:
        return '0'.zfill(length)

    digits = []
    while number > 0:
        digits.append(str(number % base))
        number //= base
    return ''.join(reversed(digits)).zfill(length)

def compute(L, binary_number, numb):
    L = list(reversed(L))
    for c in binary_number:
        x = L.pop()
        y = L.pop()
        if c == '1':
            z = x * y
        elif c == '2':
            z = int(str(x) + str(y))
        else:
            z = x + y
        if z > numb:
            return 0
        L.append(z)
    return L[0]

def part_1(lines):
    base = 2
    cnt = 0
    for line in lines:
        numb, L = line.split(':')
        numb = int(numb)
        L = [int(n) for n in L.split()]
        n = len(L) - 1

        for i in range(base ** n):
            binary = convert_base(i, base, n)
            if compute(L[:], binary, numb) == numb:
                cnt += numb
                break
    return cnt

def part_2(lines):
    base = 3
    cnt = 0
    for line in lines:
        numb, L = line.split(':')
        numb = int(numb)
        L = [int(n) for n in L.split()]
        n = len(L) - 1

        for i in range(base ** n):
            binary = convert_base(i, base, n)
            if compute(L[:], binary, numb) == numb:
                cnt += numb
                break
    return cnt
# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
