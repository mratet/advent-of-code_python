from aocd import get_data

input = get_data(day=20, year=2020)

from collections import defaultdict
from itertools import product
from math import prod, sqrt
import re

SEA_MONSTERS = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]


# WRITE YOUR SOLUTION HERE
def parse_tiles(input):
    tile_regex = r"Tile (\d+):\n((?:[.#]+\n?)+)"
    tiles = {}
    for match in re.finditer(tile_regex, input):
        tile_id = int(match.group(1))
        tile_data = match.group(2).strip().split("\n")
        tiles[tile_id] = tile_data

    return tiles


def rot_90(l):
    return ["".join(reversed(x)) for x in zip(*l)]


def vertical_flip(l):
    return ["".join(reversed(x)) for x in l]


def remove_border(tile):
    return [row[1:-1] for row in tile[1:-1]]


def get_all_image_variations(tile):
    var = {"0": tile, "0f": vertical_flip(tile)}
    for i in range(3):
        tile = rot_90(tile)
        var.update({f"{str(i + 1)}": tile, f"{str(i + 1)}f": vertical_flip(tile)})
    return var


def match_tiles(tile_1, tile_2):
    return (
        tile_1[0] == tile_2[-1]
        or tile_1[-1] == tile_2[0]
        or rot_90(tile_1)[0] == rot_90(tile_2)[-1]
        or rot_90(tile_1)[-1] == rot_90(tile_2)[0]
    )


def complete_image(tiles, mapping, starting_tile):
    n = int(sqrt(len(tiles)))
    available_tiles = set(tiles)
    image = [["."] * n for _ in range(n)]
    solution = []

    # Init
    image[0][0] = starting_tile
    available_tiles.remove(starting_tile[0])

    def backtrack(s):
        if s == n**2:
            copy = [[c for c in row] for row in image]
            solution.append(copy)
            return

        i, j = s // n, s % n

        neigh = []
        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            li, lj = i + di, j + dj
            if 0 <= li < n and 0 <= lj < n and image[li][lj] != ".":
                neigh.append(image[li][lj])

        ref_tiles = [tiles[ref_id][ref_var] for (ref_id, ref_var) in neigh]
        (ref_id, ref_var) = neigh.pop()

        for next_id in mapping[ref_id]:
            if next_id in available_tiles:
                for v_id, v_tile in tiles[next_id].items():
                    if all([match_tiles(ref_tile, v_tile) for ref_tile in ref_tiles]):
                        image[i][j] = (next_id, v_id)
                        available_tiles.remove(next_id)

                        backtrack(s + 1)

                        available_tiles.add(next_id)
                        image[i][j] = "."

    backtrack(1)
    return solution


def count_sea_monsters(full_image):
    image_width, image_size = len(full_image), len(full_image[0])
    monster_width, monster_size = len(SEA_MONSTERS), len(SEA_MONSTERS[0])
    monster_cnt = 0

    for i in range(image_width - monster_width + 1):
        for j in range(image_size - monster_size + 1):
            monster_match = [
                full_image[i + k][j + l]
                for k in range(monster_width)
                for l in range(monster_size)
                if SEA_MONSTERS[k][l] == "#"
            ]
            monster_cnt += int(
                monster_match.count("#") == "".join(SEA_MONSTERS).count("#")
            )

    return monster_cnt


def construct_full_images(tiles, image_arrangement):
    full_image = []
    (random_tile_id, random_tile_mode) = image_arrangement[0][0]
    ref_size = len(tiles[random_tile_id][random_tile_mode])

    for full_row in image_arrangement:
        image = ["" for _ in range(ref_size)]
        for tile_id, tile_mode in full_row:
            tile = tiles[tile_id][tile_mode]
            for i, row in enumerate(tile):
                image[i] = image[i] + row
        full_image.extend(image)

    return full_image


def get_adjacent_tiles(tiles):
    mapping = defaultdict(set)
    for t_id1, t_id2 in product(tiles, repeat=2):
        if t_id1 == t_id2:
            continue
        for (mode_id1, v1), (mode_id2, v2) in product(
            tiles[t_id1].items(), tiles[t_id2].items()
        ):
            if match_tiles(v1, v2):
                mapping[t_id1].add(t_id2)
    return mapping


def part_1(lines):
    init_tiles = parse_tiles(lines)
    tiles = {
        tile_id: get_all_image_variations(tile)
        for (tile_id, tile) in init_tiles.items()
    }
    mapping = get_adjacent_tiles(tiles)
    return prod(
        [tile_id for tile_id, neighbors in mapping.items() if len(neighbors) == 2]
    )


def part_2(lines):
    init_tiles = parse_tiles(lines)
    tiles = {
        tile_id: get_all_image_variations(tile)
        for (tile_id, tile) in init_tiles.items()
    }
    borderless_tiles = {
        tile_id: {mode: remove_border(tile) for mode, tile in tiles[tile_id].items()}
        for tile_id in tiles
    }

    mapping = get_adjacent_tiles(tiles)
    corner_tile = [
        tile_id for tile_id, neighbors in mapping.items() if len(neighbors) == 2
    ]

    upper_left_corner = corner_tile[0]
    for mode in ["0", "0f", "1", "1f", "2", "2f", "3", "3f"]:
        starting_tile = (upper_left_corner, mode)
        # complete_image returns 2 images :
        # - [[ul_c, ...ur_c], [....], [dl_c, ...., dr_c]]
        # - [[ul_c, ...dl_c], [....], [ur_c, ...., dr_c]] i.e same corner but flip according to the main diag
        res = complete_image(tiles, mapping, starting_tile)[0]
        full_image = construct_full_images(borderless_tiles, res)
        for tile in get_all_image_variations(full_image).values():
            c = count_sea_monsters(tile)
            if c:
                return (
                    sum([row.count("#") for row in full_image])
                    - "".join(SEA_MONSTERS).count("#") * c
                )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
