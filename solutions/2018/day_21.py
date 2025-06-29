from aocd import get_data

input = get_data(day=21, year=2018).splitlines()


def get_personal_input(lines):
    _, true_val, *_ = lines[8].split()
    return int(true_val)


def real_program(true_val):
    reg6 = 0
    function = lambda x: ((x & 16777215) * 65899) & 16777215
    seen = []
    while True:
        reg4 = reg6 | 65536
        reg6 = true_val

        while reg4 > 0:
            reg6 = function(reg6 + (reg4 & 255))
            reg4 = reg4 // 256
        if reg6 in seen:
            break
        seen.append(reg6)
    return seen


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    personal_input = get_personal_input(lines)
    halt_values = real_program(personal_input)
    return halt_values[0]


def part_2(lines):
    personal_input = get_personal_input(lines)
    halt_values = real_program(personal_input)
    return halt_values[-1]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
