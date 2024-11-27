from aocd import get_data
input = get_data(day=4, year=2020).split('\n\n')
import re

# WRITE YOUR SOLUTION HERE
MANDATORY_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def part_1(lines):
    cnt = 0
    for line in lines:
        passport = {field.split(':')[0]: field.split(':')[1] for field in line.replace('\n', ' ').split(' ')}
        cnt += (not MANDATORY_FIELDS - set(passport))
    return cnt

def part_2(lines):
    REQUIREMENTS = [
        ("byr", lambda x: 1920 <= int(x) <= 2002),
        ("iyr", lambda x: 2010 <= int(x) <= 2020),
        ("eyr", lambda x: 2020 <= int(x) <= 2030),
        (
            "hgt",
            lambda x: (x.endwith("cm") and 150 <= int(x[:-2]) <= 193)
                      or (x.endwith("in") and 59 <= int(x[:-2]) <= 76),
        ),
        ("hcl", lambda x: re.fullmatch(r"#[0-9a-f]{6}", x)),
        ("ecl", lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
        ("pid", lambda x: re.fullmatch(r"[0-9]{9}", x)),
    ]

    cnt = 0
    for line in lines:
        passport = {field.split(':')[0]: field.split(':')[1] for field in line.replace('\n', ' ').split(' ')}
        if not MANDATORY_FIELDS - set(passport):
            cnt += all(req(passport[key]) for key, req in REQUIREMENTS)
    return cnt

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')

