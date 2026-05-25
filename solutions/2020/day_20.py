import re
from collections import defaultdict
from math import prod, sqrt

from aocd import get_data

input = get_data(day=20, year=2020)

SEA_MONSTERS = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
MONSTER_CELLS = [(k, l) for k, row in enumerate(SEA_MONSTERS) for l, c in enumerate(row) if c == "#"]
MONSTER_COUNT = len(MONSTER_CELLS)


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
    return ["".join(reversed(x)) for x in zip(*l, strict=False)]


def vertical_flip(l):
    return ["".join(reversed(x)) for x in l]


def remove_border(tile):
    return [row[1:-1] for row in tile[1:-1]]


def get_all_image_variations(tile):
    var = {"0": tile, "0f": vertical_flip(tile)}
    for i in range(3):
        tile = rot_90(tile)
        var.update({f"{i + 1}": tile, f"{i + 1}f": vertical_flip(tile)})
    return var


def match_tiles(tile_1, tile_2):
    r1, r2 = rot_90(tile_1), rot_90(tile_2)
    return tile_1[0] == tile_2[-1] or tile_1[-1] == tile_2[0] or r1[0] == r2[-1] or r1[-1] == r2[0]


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
            copy = [list(row) for row in image]
            solution.append(copy)
            return True

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
                    if all(match_tiles(ref_tile, v_tile) for ref_tile in ref_tiles):
                        image[i][j] = (next_id, v_id)
                        available_tiles.remove(next_id)

                        if backtrack(s + 1):
                            return True

                        available_tiles.add(next_id)
                        image[i][j] = "."

    backtrack(1)
    return solution


def count_sea_monsters(full_image):
    image_width, image_size = len(full_image), len(full_image[0])
    monster_height = len(SEA_MONSTERS)
    monster_width = len(SEA_MONSTERS[0])
    monster_cnt = 0

    for i in range(image_width - monster_height + 1):
        for j in range(image_size - monster_width + 1):
            if all(full_image[i + k][j + l] == "#" for k, l in MONSTER_CELLS):
                monster_cnt += 1

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


def get_edges(tile):
    top, bottom = tile[0], tile[-1]
    left = "".join(row[0] for row in tile)
    right = "".join(row[-1] for row in tile)
    edges = [top, bottom, left, right]
    return edges + [e[::-1] for e in edges]


def get_adjacent_tiles(init_tiles):
    edge_to_tiles = defaultdict(set)
    for tile_id, tile in init_tiles.items():
        for edge in get_edges(tile):
            edge_to_tiles[edge].add(tile_id)
    mapping = defaultdict(set)
    for tile_ids in edge_to_tiles.values():
        for t1 in tile_ids:
            for t2 in tile_ids:
                if t1 != t2:
                    mapping[t1].add(t2)
    return mapping


def part_1(lines):
    init_tiles = parse_tiles(lines)
    mapping = get_adjacent_tiles(init_tiles)
    return prod(tile_id for tile_id, neighbors in mapping.items() if len(neighbors) == 2)


def part_2(lines):
    init_tiles = parse_tiles(lines)
    tiles = {tile_id: get_all_image_variations(tile) for (tile_id, tile) in init_tiles.items()}
    borderless_tiles = {
        tile_id: {mode: remove_border(tile) for mode, tile in tiles[tile_id].items()} for tile_id in tiles
    }

    mapping = get_adjacent_tiles(init_tiles)
    corner_tile = [tile_id for tile_id, neighbors in mapping.items() if len(neighbors) == 2]

    upper_left_corner = corner_tile[0]
    for mode in tiles[upper_left_corner]:
        starting_tile = (upper_left_corner, mode)
        # complete_image returns 2 images :
        # - [[ul_c, ...ur_c], [....], [dl_c, ...., dr_c]]
        # - [[ul_c, ...dl_c], [....], [ur_c, ...., dr_c]] i.e same corner but flip according to the main diag
        res = complete_image(tiles, mapping, starting_tile)[0]
        full_image = construct_full_images(borderless_tiles, res)
        for tile in get_all_image_variations(full_image).values():
            c = count_sea_monsters(tile)
            if c:
                return sum(row.count("#") for row in full_image) - MONSTER_COUNT * c


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
