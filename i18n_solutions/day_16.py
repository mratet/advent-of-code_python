from blessed import Terminal
from dataclasses import dataclass

from typing import List
import sys


@dataclass
class PieceType:
    """Definition of a piece type with its rotation behavior"""

    char: str
    rotates_to: str
    right: int
    down: int
    left: int
    up: int
    _rotation_count: int = None

    @property
    def rotation_count(self):
        if self._rotation_count is None:
            curr_char, count = self.char, 0
            while True:
                curr_char = PIECE_TYPES[curr_char].rotates_to
                count += 1
                if curr_char == self.char:
                    self._rotation_count = count - 1
                    return self._rotation_count
        return self._rotation_count


PIECE_TYPES = {
    "┌": PieceType("┌", "┐", 1, 1, 0, 0),
    "┐": PieceType("┐", "┘", 0, 1, 1, 0),
    "┘": PieceType("┘", "└", 0, 0, 1, 1),
    "└": PieceType("└", "┌", 1, 0, 0, 1),
    "├": PieceType("├", "┬", 1, 1, 0, 1),
    "┬": PieceType("┬", "┤", 1, 1, 1, 0),
    "┤": PieceType("┤", "┴", 0, 1, 1, 1),
    "┴": PieceType("┴", "├", 1, 0, 1, 1),
    "│": PieceType("│", "─", 0, 1, 0, 1),
    "─": PieceType("─", "│", 1, 0, 1, 0),
    "┼": PieceType("┼", "┼", 1, 1, 1, 1),
    "╔": PieceType("╔", "╗", 2, 2, 0, 0),
    "╗": PieceType("╗", "╝", 0, 2, 2, 0),
    "╝": PieceType("╝", "╚", 0, 0, 2, 2),
    "╚": PieceType("╚", "╔", 2, 0, 0, 2),
    "╠": PieceType("╠", "╦", 2, 2, 0, 2),
    "╦": PieceType("╦", "╣", 2, 2, 2, 0),
    "╣": PieceType("╣", "╩", 0, 2, 2, 2),
    "╩": PieceType("╩", "╠", 2, 0, 2, 2),
    "║": PieceType("║", "═", 0, 2, 0, 2),
    "═": PieceType("═", "║", 2, 0, 2, 0),
    "╬": PieceType("╬", "╬", 2, 2, 2, 2),
    "╟": PieceType("╟", "╤", 1, 2, 0, 2),
    "╤": PieceType("╤", "╢", 2, 1, 2, 0),
    "╢": PieceType("╢", "╧", 0, 2, 1, 2),
    "╧": PieceType("╧", "╟", 2, 0, 2, 1),
    "╞": PieceType("╞", "╥", 2, 1, 0, 1),
    "╥": PieceType("╥", "╡", 1, 2, 1, 0),
    "╡": PieceType("╡", "╨", 0, 1, 2, 1),
    "╨": PieceType("╨", "╞", 1, 0, 1, 2),
    "╒": PieceType("╒", "╖", 2, 1, 0, 0),
    "╖": PieceType("╖", "╛", 0, 2, 1, 0),
    "╛": PieceType("╛", "╙", 0, 0, 2, 1),
    "╙": PieceType("╙", "╒", 1, 0, 0, 2),
    "╓": PieceType("╓", "╕", 1, 2, 0, 0),
    "╕": PieceType("╕", "╜", 0, 1, 2, 0),
    "╜": PieceType("╜", "╘", 0, 0, 1, 2),
    "╘": PieceType("╘", "╓", 2, 0, 0, 1),
    "╫": PieceType("╫", "╪", 1, 2, 1, 2),
    "╪": PieceType("╪", "╫", 2, 1, 2, 1),
    " ": PieceType(" ", " ", 0, 0, 0, 0),
}


@dataclass
class Piece:
    """An instance of a piece in the game"""

    type_char: str
    rotation: int = 0  # Number of rotations from base position
    fixed: bool = False

    def __post_init__(self):
        if self.type_char not in PIECE_TYPES:
            raise ValueError(f"Invalid piece type: {self.type_char}")

    @property
    def char(self):
        return self._get_rotated_type().char

    @property
    def right(self):
        return self._get_rotated_type().right

    @property
    def down(self):
        return self._get_rotated_type().down

    @property
    def left(self):
        return self._get_rotated_type().left

    @property
    def up(self):
        return self._get_rotated_type().up

    @property
    def rotation_count(self):
        return PIECE_TYPES[self.type_char].rotation_count

    def _get_rotated_type(self):
        curr_char = self.type_char
        for _ in range(self.rotation):
            curr_char = PIECE_TYPES[curr_char].rotates_to
        return PIECE_TYPES[curr_char]

    def is_connected_to_neighbor(self, neighbor, direction):
        if direction == "right":
            return self.right > 0 and neighbor.left > 0 and self.right == neighbor.left
        elif direction == "down":
            return self.down > 0 and neighbor.up > 0 and self.down == neighbor.up
        elif direction == "left":
            return self.left > 0 and neighbor.right > 0 and self.left == neighbor.right
        elif direction == "up":
            return self.up > 0 and neighbor.down > 0 and self.up == neighbor.down
        return False

    def rotate(self, n: int):
        if self.rotation_count == 0:
            return Piece(self.type_char, self.fixed)

        new_rotation = (self.rotation + n) % (self.rotation_count + 1)
        return Piece(self.type_char, new_rotation, self.fixed)


class PipeGame:
    def __init__(self, input_file: str):
        self.term = Terminal()
        self.grid = self.load_grid(input_file)
        self.height, self.width = len(self.grid), len(self.grid[0])
        self.cursor = [1, 1]
        self.cheat_mode = False
        self.grid[0][1].fixed = self.grid[-1][-2].fixed = True

    def load_grid(self, file_path: str) -> List[List[Piece]]:
        try:
            with open(file_path, "r") as f:
                rows = f.read().splitlines()
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            sys.exit(1)

        X_start, X_end = 6, -6
        Y_start, Y_end = 4, -5
        grid = []
        for row in rows[Y_start:Y_end]:
            line = bytes([ord(c) for c in row]).decode("cp437")[X_start:X_end]
            grid_row = []
            for c in line:
                type_char = c if c in PIECE_TYPES else " "
                fixed = type_char in ["┼", "╬", " "]
                grid_row.append(Piece(type_char, fixed=fixed))
            grid.append(grid_row)
        return grid

    def compute_score(self) -> int:
        return sum(
            self.grid[y][x].rotation
            for y in range(self.height)
            for x in range(self.width)
        )

    def display_all_grid(self):
        print(self.term.clear)
        print(self.term.bold("Pipe Puzzle Game"))
        print(
            self.term.bold(
                "hjkl: Move cursor | r: Rotate tile | f: Fix tile | c: Enable Cheat Mode | q: Quit"
            )
        )
        print(self.term.bold(f"Score: {self.compute_score()}"))
        print(self.term.bold("-" * 40))
        print()

        for y in range(self.height):
            for x in range(self.width):
                symb = self.get_colored_tile(self.grid[y][x], [x, y])
                print(symb, end="")
            print()

    def is_piece_connected(self, cursor) -> bool:
        x, y = cursor
        piece = self.grid[y][x]

        neighboors = {
            "right": [x + 1, y],
            "down": [x, y + 1],
            "left": [x - 1, y],
            "up": [x, y - 1],
        }

        for direction, (nx, ny) in neighboors.items():
            dir_value = getattr(piece, direction)
            if dir_value == 0:
                continue

            if not (0 <= nx < self.width and 0 <= ny < self.height):
                return False

            neighbor = self.grid[ny][nx]
            if not piece.is_connected_to_neighbor(neighbor, direction):
                return False

        return True

    def get_colored_tile(self, piece: Piece, cursor: List[int]) -> str:
        if cursor == self.cursor:
            return self.term.yellow(piece.char)
        elif self.cheat_mode:
            return (
                self.term.green(piece.char)
                if self.is_piece_connected(cursor)
                else self.term.red(piece.char)
            )
        elif piece.fixed:
            return self.term.blue(piece.char)
        else:
            return piece.char

    def update_single_tile(self, unk_cursor: List[int]):
        x, y = unk_cursor
        symb = self.get_colored_tile(self.grid[y][x], unk_cursor)
        with self.term.location(x, y + 6):
            print(symb, end="", flush=True)

    def rotate_tile(self):
        x, y = self.cursor
        piece = self.grid[y][x]
        if piece.fixed:
            return
        self.grid[y][x] = piece.rotate(1)
        self.update_single_tile(self.cursor)
        self.update_score()
        if self.cheat_mode:
            for adj_x, adj_y in ([x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]):
                if 0 <= adj_x < self.width and 0 <= adj_y < self.height:
                    self.update_single_tile([adj_x, adj_y])

    def update_score(self):
        with self.term.location(0, 3):
            print(
                self.term.clear_eol + self.term.bold(f"Score: {self.compute_score()}"),
                end="",
                flush=True,
            )

    def move_cursor(self, dx: int, dy: int):
        x, y = self.cursor
        nex_x, nex_y = x + dx, y + dy
        if 0 < nex_x < self.width - 1 and 0 < nex_y < self.height - 1:
            self.cursor = [nex_x, nex_y]

        self.update_single_tile(self.cursor)
        self.update_single_tile([x, y])

    def toggle_cheat_mode(self):
        self.cheat_mode = not self.cheat_mode
        self.display_all_grid()

    def toggle_fixed(self):
        x, y = self.cursor
        current_piece = self.grid[y][x]
        self.grid[y][x] = Piece(
            current_piece.type_char, current_piece.rotation, not current_piece.fixed
        )
        self.update_single_tile(self.cursor)

    def check_all_connected(self) -> bool:
        return all(
            self.is_piece_connected([x, y])
            for y in range(self.height)
            for x in range(self.width)
        )

    def run(self):
        with self.term.cbreak(), self.term.hidden_cursor():
            self.display_all_grid()
            while True:
                key = self.term.inkey()
                if key == "q":
                    break
                elif key == "k":
                    self.move_cursor(0, -1)
                elif key == "j":
                    self.move_cursor(0, 1)
                elif key == "h":
                    self.move_cursor(-1, 0)
                elif key == "l":
                    self.move_cursor(1, 0)
                elif key == "r":
                    self.rotate_tile()
                elif key == "f":
                    self.toggle_fixed()
                elif key == "c":
                    self.toggle_cheat_mode()


game = PipeGame("input.txt")
game.run()
