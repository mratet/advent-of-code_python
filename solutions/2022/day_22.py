import re
from collections import namedtuple

from aocd import get_data

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


# Face layout (specific to this puzzle input):
#  12
#  3
# 45
#  6
# Board uses face-relative coordinates (face_id, x, y) with x, y in [0, FACE_SIZE).
# Edge transitions and coordinate transforms are hardcoded for this input's cube folding.

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

_S = FACE_SIZE - 1
COORD_TRANSFORMS = {
    "1R": lambda x, y: (0, y),
    "4R": lambda x, y: (0, y),
    "2L": lambda x, y: (_S, y),
    "5L": lambda x, y: (_S, y),
    "1D": lambda x, y: (x, 0),
    "3D": lambda x, y: (x, 0),
    "4D": lambda x, y: (x, 0),
    "6D": lambda x, y: (x, 0),
    "2U": lambda x, y: (x, _S),
    "3U": lambda x, y: (x, _S),
    "5U": lambda x, y: (x, _S),
    "6U": lambda x, y: (x, _S),
    "1L": lambda x, y: (x, _S - y),
    "4L": lambda x, y: (x, _S - y),
    "2R": lambda x, y: (x, _S - y),
    "5R": lambda x, y: (x, _S - y),
    "1U": lambda x, y: (y, x),
    "2D": lambda x, y: (y, x),
    "3R": lambda x, y: (y, x),
    "3L": lambda x, y: (y, x),
    "4U": lambda x, y: (y, x),
    "5D": lambda x, y: (y, x),
    "6R": lambda x, y: (y, x),
    "6L": lambda x, y: (y, x),
}


# WRITE YOUR SOLUTION HERE
def build_face_map(grid):
    face_map = {}
    face_id = 1
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != " ":
                key = (x // FACE_SIZE, y // FACE_SIZE)
                if key not in face_map:
                    face_map[key] = face_id
                    face_id += 1
    return face_map


def get_face_id(x, y, face_map):
    return face_map.get((x // FACE_SIZE, y // FACE_SIZE))


def get_real_coords(pos, inv_map):
    fid, x, y = pos
    fx, fy = inv_map[fid]
    return x + fx * FACE_SIZE, y + fy * FACE_SIZE


def parse_input(raw_input):
    board_text, path_text = raw_input.split("\n\n")
    face_map = build_face_map(board_text.split("\n"))
    board = {}
    for y, line in enumerate(board_text.splitlines()):
        for x, c in enumerate(line):
            if c != " ":
                fid = get_face_id(x, y, face_map)
                board[(fid, x % FACE_SIZE, y % FACE_SIZE)] = c
    path = [(int(num), turn) for num, turn in re.findall(r"(\d+)([RL]?)", path_text)]
    return board, path, face_map


def wrap_position(pos, dir_idx, part):
    fid, x, y = pos
    direction = DIRECTIONS[dir_idx]
    transitions = FACE_TRANSITION_PART1 if part == "part_1" else FACE_TRANSITION_PART2
    new_fid, arrival_dir = transitions[(fid, direction.letter)]
    sid = f"{fid}{direction.letter}"
    if part == "part_1":
        x = FACE_SIZE - 1 if direction.letter == "L" else 0 if direction.letter == "R" else x
        y = FACE_SIZE - 1 if direction.letter == "U" else 0 if direction.letter == "D" else y
    else:
        x, y = COORD_TRANSFORMS[sid](x, y)
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


def solve(lines, part="part_1"):
    board, path, face_map = parse_input(lines)
    inv_map = {v: k for k, v in face_map.items()}
    pos, dir_idx = simulate(board, path, part)
    rx, ry = get_real_coords(pos, inv_map)
    return 1000 * (ry + 1) + 4 * (rx + 1) + dir_idx


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
