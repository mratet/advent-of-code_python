from collections import namedtuple

from aocd import get_data
import re

input = get_data(day=22, year=2022)
FACE_SIZE = 50


Direction = namedtuple("Direction", ["dx", "dy", "letter"])
DIRECTIONS = [
    Direction(1, 0, "R"),
    Direction(0, 1, "D"),
    Direction(-1, 0, "L"),
    Direction(0, -1, "U"),
]
LETTER_TO_DIR = {d.letter: i for i, d in enumerate(DIRECTIONS)}
VECTOR_TO_LETTER = {(d.dx, d.dy): d.letter for d in DIRECTIONS}


def transition_dict(pairs):
    d = {}
    for k, v in pairs.items():
        from_fid, from_dir = int(k[0]), k[1]
        to_fid, to_dir = int(v[0]), v[1]
        d[(from_fid, from_dir)] = (to_fid, to_dir)
        d[(to_fid, to_dir)] = (from_fid, from_dir)
    return d


FACE_TRANSITION_PART1 = transition_dict(
    {
        "1R": "2L",
        "2R": "1L",
        "3R": "3L",
        "4R": "5L",
        "5R": "4L",
        "6R": "6L",
        "1U": "5D",
        "2U": "2D",
        "3U": "1D",
        "4U": "6D",
        "5U": "3D",
        "6U": "4D",
    }
)

FACE_TRANSITION_PART2 = transition_dict(
    {
        "1R": "2L",
        "1D": "3U",
        "1L": "4L",
        "1U": "6L",
        "4D": "6U",
        "2D": "3R",
        "4U": "3L",
        "2U": "6D",
        "5R": "2R",
        "5D": "6R",
        "5L": "4R",
        "5U": "3D",
    }
)


def build_face_map(grid):
    face_map = {}
    face_id = 1
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != " ":
                tile_x = x // FACE_SIZE
                tile_y = y // FACE_SIZE
                key = (tile_x, tile_y)
                if key not in face_map:
                    face_map[key] = face_id
                    face_id += 1
    return face_map


def get_face_id(x, y, face_map, face_size=FACE_SIZE):
    return face_map.get(
        ((x // face_size), (y // face_size)), None
    )  # None si hors des faces


def get_real_coords(pos, face_map, face_size=FACE_SIZE):
    fid, x, y = pos
    inv_map = {v: k for k, v in face_map.items()}
    fx, fy = inv_map[fid]
    return x + fx * face_size, y + fy * face_size


def parse_input(raw_input):
    board_text, path_text = raw_input.split("\n\n")
    face_map = build_face_map(board_text.split("\n"))

    board = {}
    for y, line in enumerate(board_text.splitlines()):
        for x, c in enumerate(line):
            if c != " ":
                fid = get_face_id(x, y, face_map)
                board[(fid, x % FACE_SIZE, y % FACE_SIZE)] = c

    matches = parse_path(path_text)
    return board, matches, face_map


def parse_path(path_text):
    matches = re.findall(r"(\d+)([RL]?)", path_text)
    return [(int(num), turn) for num, turn in matches]


def wrap_position(pos, dir_idx, part):
    fid, x, y = pos
    direction = DIRECTIONS[dir_idx]
    transitions = FACE_TRANSITION_PART1 if part == "part_1" else FACE_TRANSITION_PART2
    new_fid, arrival_dir = transitions[(fid, direction.letter)]
    sid = f"{fid}{direction.letter}"

    if part == "part_1":
        x = (
            FACE_SIZE - 1
            if direction.letter == "L"
            else 0
            if direction.letter == "R"
            else x
        )
        y = (
            FACE_SIZE - 1
            if direction.letter == "U"
            else 0
            if direction.letter == "D"
            else y
        )
    elif part == "part_2":
        match sid:
            case "1R":
                x = 0
            case "1D":
                y = 0
            case "1L":
                y = FACE_SIZE - 1 - y
            case "1U":
                x, y = y, x

            case "2R":
                y = FACE_SIZE - 1 - y
            case "2D":
                x, y = y, x
            case "2L":
                x = FACE_SIZE - 1
            case "2U":
                y = FACE_SIZE - 1

            case "3R":
                x, y = y, x
            case "3D":
                y = 0
            case "3L":
                x, y = y, x
            case "3U":
                y = FACE_SIZE - 1

            case "4R":
                x = 0
            case "4D":
                y = 0
            case "4L":
                y = FACE_SIZE - 1 - y
            case "4U":
                x, y = y, x

            case "5R":
                y = FACE_SIZE - 1 - y
            case "5D":
                x, y = y, x
            case "5L":
                x = FACE_SIZE - 1
            case "5U":
                y = FACE_SIZE - 1

            case "6R":
                x, y = y, x
            case "6D":
                y = 0
            case "6L":
                x, y = y, x
            case "6U":
                y = FACE_SIZE - 1

    return (new_fid, x, y), (LETTER_TO_DIR[arrival_dir] + 2) % 4


def next_position(pos, dir_idx, board, part):
    fid, x, y = pos
    d = DIRECTIONS[dir_idx]
    nx, ny = x + d.dx, y + d.dy
    new_dir_idx = dir_idx
    if not (0 <= nx < FACE_SIZE and 0 <= ny < FACE_SIZE):
        pos, new_dir_idx = wrap_position(pos, dir_idx, part)
    else:
        pos = (fid, nx, ny)

    return (pos, new_dir_idx) if board.get(pos) != "#" else ((fid, x, y), dir_idx)


def simulate(board, path, part="part_1"):
    pos = min(board)
    dir_idx = 0
    for steps, turn in path:
        for _ in range(steps):
            pos, dir_idx = next_position(pos, dir_idx, board, part)
        if turn:
            dir_idx = (dir_idx + (1 if turn == "R" else -1)) % 4
    return pos, dir_idx


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    board, path, face_map = parse_input(lines)
    pos, dir_idx = simulate(board, path, "part_1")
    rx, ry = get_real_coords(pos, face_map)
    return 1000 * (ry + 1) + 4 * (rx + 1) + dir_idx


def part_2(lines):
    board, path, face_map = parse_input(lines)
    pos, dir_idx = simulate(board, path, "part_2")
    rx, ry = get_real_coords(pos, face_map)
    return 1000 * (ry + 1) + 4 * (rx + 1) + dir_idx


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
