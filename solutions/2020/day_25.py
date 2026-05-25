from aocd import get_data

input = get_data(day=25, year=2020).splitlines()

MOD = 20201227


# WRITE YOUR SOLUTION HERE
def research_loop_size(public_key):
    value, i = 1, 0
    while value != public_key:
        value = value * 7 % MOD
        i += 1
    return i


def part_1(lines):
    card_public_key, door_public_key = int(lines[0]), int(lines[1])
    card_loop_size = research_loop_size(card_public_key)
    door_loop_size = research_loop_size(door_public_key)
    encryption_key = pow(door_public_key, card_loop_size, MOD)
    assert encryption_key == pow(card_public_key, door_loop_size, MOD)
    return encryption_key


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
