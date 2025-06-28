from dataclasses import dataclass, field

from aocd import get_data

input = get_data(day=13, year=2018).splitlines()

DIRECTION = {
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
    "N": (0, -1),
}


LEFT_TURN = {"N": "W", "S": "E", "E": "N", "W": "S"}
RIGHT_TURN = {"N": "E", "S": "W", "E": "S", "W": "N"}
MAPPING = {">": "E", "<": "W", "v": "S", "^": "N"}


@dataclass(order=True)
class Cart:
    sort_index: tuple = field(init=False, repr=False)
    id: int
    x: int
    y: int
    direction: str
    next_turn: int = 0
    active: bool = True

    def __post_init__(self):
        self.update_sort_index()

    def move(self):
        dx, dy = DIRECTION[self.direction]
        self.x += dx
        self.y += dy
        self.update_sort_index()

    def update_sort_index(self):
        self.sort_index = (self.x, self.y)

    def turn_at_intersection(self):
        if self.next_turn == 0:
            self.direction = LEFT_TURN[self.direction]
        elif self.next_turn == 2:
            self.direction = RIGHT_TURN[self.direction]
        self.next_turn = (self.next_turn + 1) % 3

    def turn_on_curve(self, track):
        if track == "/":
            self.direction = {"N": "E", "E": "N", "S": "W", "W": "S"}[self.direction]
        elif track == "\\":
            self.direction = {"N": "W", "W": "N", "S": "E", "E": "S"}[self.direction]


def parse_input(lines):
    cart_id = 0
    carts = []
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in "<>^v":
                carts.append(Cart(cart_id, x, y, MAPPING[c]))
                grid[(x, y)] = "|" if c in "v^" else "-"
                cart_id += 1
            elif c in "-|+/\\":
                grid[(x, y)] = c
    return grid, carts


def simulate(grid, carts, stop_on_first_collision=True):
    while True:
        carts.sort()
        positions = {(c.x, c.y): c for c in carts if c.active}

        for cart in carts:
            if not cart.active:
                continue

            positions.pop((cart.x, cart.y))
            cart.move()

            pos = (cart.x, cart.y)
            if pos in positions and positions[pos].active:
                if stop_on_first_collision:
                    return pos
                else:
                    cart.active = False
                    positions[pos].active = False
                    continue

            track = grid[pos]
            if track == "+":
                cart.turn_at_intersection()
            elif track in "/\\":
                cart.turn_on_curve(track)

            positions[pos] = cart

        if not stop_on_first_collision:
            active_carts = [c for c in carts if c.active]
            if len(active_carts) == 1:
                return (active_carts[0].x, active_carts[0].y)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    grid, carts = parse_input(lines)
    x, y = simulate(grid, carts, stop_on_first_collision=True)
    return f"{x},{y}"


def part_2(lines):
    grid, carts = parse_input(lines)
    x, y = simulate(grid, carts, stop_on_first_collision=False)
    return f"{x},{y}"


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
