from aocd import get_data, submit

input = get_data(day=25, year=2020).splitlines()


# WRITE YOUR SOLUTION HERE
def handshake(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value


def research_loop_size(public_key):
    value = 1
    i = 0
    while value != public_key:
        value = (value * 7) % 20201227
        i += 1
    return i


def part_1(lines):
    card_public_key, door_public_key = int(lines[0]), int(lines[1])
    card_loop_size = research_loop_size(card_public_key)
    door_loop_size = research_loop_size(door_public_key)

    encryption_key = handshake(card_public_key, door_loop_size)
    assert encryption_key == handshake(door_public_key, card_loop_size)

    return encryption_key


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
