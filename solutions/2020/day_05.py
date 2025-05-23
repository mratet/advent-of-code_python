from aocd import get_data

input = get_data(day=5, year=2020).splitlines()


# WRITE YOUR SOLUTION HERE
def compute_seat_position(seat):
    rows = seat[:7].replace("F", "0").replace("B", "1")
    columns = seat[7:].replace("L", "0").replace("R", "1")
    return int(rows, 2) * 8 + int(columns, 2)


def part_1(lines):
    return max([compute_seat_position(line) for line in lines])


def part_2(lines):
    empty_seat = set(range(127 * 8 + 7)) - set(
        compute_seat_position(line) for line in lines
    )
    for seat in empty_seat:
        if (seat + 1 not in empty_seat) and (seat - 1 not in empty_seat):
            return seat


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
