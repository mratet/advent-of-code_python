import time

from aocd import get_data
from intcode import IntcodeComputer
from itertools import batched

from blessed import Terminal

aoc_input = get_data(day=13, year=2019)


class IntcodeGUI:
    def __init__(self, program_file: str, playing_type: int = 0):
        self.term = Terminal()
        self.computer = IntcodeComputer(program_file)
        self.grid: dict[tuple[int, int], int] = {}
        self.score = 0
        self.ball_pos = (0, 0)
        self.paddle_pos = (0, 0)
        self.playing_type = playing_type

        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0

    def draw_initial_screen(self):
        print(self.term.clear)
        with self.term.location(0, 0):
            print(self.term.bold("arcade intcode - day 13 aoc 2019"))
        with self.term.location(0, 1):
            print(self.term.bold("s: left | f: right | q: quit"))
        with self.term.location(0, 2):
            print(self.term.bold(f"score: {self.score}"))
        with self.term.location(0, 3):
            print(self.term.bold("-" * 40))

        # Initial drawing of the grid if it exists, otherwise it will be drawn by update_tile
        if self.grid:
            self.min_x = min(k[0] for k in self.grid.keys())
            self.max_x = max(k[0] for k in self.grid.keys())
            self.min_y = min(k[1] for k in self.grid.keys())
            self.max_y = max(k[1] for k in self.grid.keys())

            tile_map = {0: " ", 1: "█", 2: "▒", 3: self.term.bold_blue("_"), 4: "●"}

            for y in range(self.min_y, self.max_y + 1):
                with self.term.location(self.min_x, y + 5):  # +5 to offset the header
                    for x in range(self.min_x, self.max_x + 1):
                        tile_id = self.grid.get((x, y), 0)
                        print(tile_map[tile_id], end="")
                    print(self.term.clear_eol)

    def update_tile(self, x: int, y: int, tile_id: int):
        self.grid[(x, y)] = tile_id
        if tile_id == 4:
            self.ball_pos = (x, y)
        elif tile_id == 3:
            self.paddle_pos = (x, y)

        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)

        tile_map = {0: " ", 1: "█", 2: "▒", 3: self.term.bold_blue("_"), 4: "●"}
        char = tile_map.get(tile_id, " ")

        with self.term.location(x, y + 5):  # +5 to offset the header lines
            print(char, end="", flush=True)

    def update_score(self, new_score: int):
        self.score = new_score
        with self.term.location(0, 2):
            print(
                self.term.clear_eol + self.term.bold(f"score: {self.score}"),
                end="",
                flush=True,
            )

    def run(self):
        self.computer.memory[0] = 2

        initial_output = self.computer.run()
        for x, y, tile_id in batched(initial_output, n=3):
            if x == -1 and y == 0:
                self.update_score(tile_id)
            else:
                self.grid[(x, y)] = tile_id

        self.draw_initial_screen()

        joystick = 0
        with self.term.cbreak(), self.term.hidden_cursor():
            while not self.computer.hasted:
                output = self.computer.run([joystick])
                for x, y, tile_id in batched(output, n=3):
                    if x == -1 and y == 0:
                        self.update_score(tile_id)
                    else:
                        self.update_tile(x, y, tile_id)

                if self.playing_type == 0:
                    key = self.term.inkey(timeout=0.001)
                    if key == "q":
                        break
                    elif key == "s":
                        joystick = -1
                    elif key == "f":
                        joystick = 1
                    else:
                        joystick = 0
                elif self.playing_type == 1:
                    time.sleep(0.001)
                    if self.ball_pos[0] < self.paddle_pos[0]:
                        joystick = -1
                    elif self.ball_pos[0] > self.paddle_pos[0]:
                        joystick = 1
                    else:
                        joystick = 0

        return self.score


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    pc = IntcodeComputer(lines)
    tiles = pc.run()
    return sum(tile_id == 2 for _, _, tile_id in batched(tiles, 3))


def part_2(lines):
    # Use playing_type 0 if you want to play
    gui = IntcodeGUI(program_file=lines, playing_type=1)
    return gui.run()


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
