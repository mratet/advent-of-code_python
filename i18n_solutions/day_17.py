from typing import List, Dict

from functools import reduce

import itertools
from collections import defaultdict

# 4 on test_input, 8 on puzzle_input
MAGIC_NUMBER = 8
REPLACEMENT_CHAR = chr(65533)


class Block:
    def __init__(self, raw_block: str):
        self.raw_block = raw_block
        self._rows = self.raw_block.split("\n")
        self.decoded_block = self.decode_block()
        self._decoded_rows = self.decoded_block.split("\n")
        self.height = len(self._rows)
        self.width = len(self._rows[0])

    def get_treasure_coordinates(self):
        for row_idx, row in enumerate(self._decoded_rows):
            if "╳" in row:
                return row_idx, row.index("╳")
        return -1

    def decode_block(self) -> str:
        return "\n".join(
            bytes.fromhex(row).decode("utf-8", "replace") for row in self._rows
        )

    def has_replacement_in_junction(self):
        for row in self._decoded_rows:
            if REPLACEMENT_CHAR in row[3:-3]:
                return True
        return False

    def merge_vertical(self, other: "Block") -> "Block":
        return Block(f"{self.raw_block}\n{other.raw_block}")

    def merge_horizontal(self, other: "Block") -> "Block":
        if self.height != other.height:
            raise ValueError("Blocks must have same height for horizontal merge")
        merged_rows = [p + q for p, q in zip(self._rows, other._rows)]
        return Block("\n".join(merged_rows))

    def convolve(self, other: "Block") -> defaultdict[int, list[str]]:
        n1, n2 = len(self._rows), len(other._rows)
        res = defaultdict(list)
        other_rows = other._rows[::-1]
        for i, j in itertools.product(range(n1), range(n2)):
            # Depends on how blocks were divided for the puzzle
            if (i + j + 1) % MAGIC_NUMBER == 0:
                res[i + j].append(self._rows[i] + other_rows[j])
        return res

    def match(self, other):
        convolved = self.convolve(other)
        for k, c_block in convolved.items():
            d_block = Block("\n".join(c_block))
            if not d_block.has_replacement_in_junction():
                return k
        return 0


def identify_relevant_blocks(blocks_dict: dict):
    top_left_corner, bottom_left_corner = None, None
    left_edges = []
    for block_id, block in blocks_dict.items():
        if "╔" in block.decoded_block:
            top_left_corner = block_id
        elif "╚" in block.decoded_block:
            bottom_left_corner = block_id
        elif "\n║" in block.decoded_block:
            left_edges.append(block_id)
    return top_left_corner, bottom_left_corner, left_edges


def build_column_block(col_blocks: List[Block]) -> Block:
    first_block = col_blocks.pop(0)
    return reduce(lambda x, y: x.merge_vertical(y), col_blocks, first_block)


def build_row_block(row_blocks: List[Block]) -> Block:
    first_block = row_blocks.pop(0)
    return reduce(lambda x, y: x.merge_horizontal(y), row_blocks, first_block)


def build_columns(blocks_dict: Dict[int, Block], first_col_ids: List[int]):
    block_ids = set(blocks_dict) - set(first_col_ids)
    first_block = build_column_block([blocks_dict[id] for id in first_col_ids])
    column_blocks = [first_block]
    while block_ids:
        block = column_blocks[-1]
        right_block_ids = []
        for block_id in block_ids:
            k = block.match(blocks_dict[block_id])
            if k > 0:
                right_block_ids.append((k, block_id))
        sorted_ids = [id for (_, id) in sorted(right_block_ids, key=lambda x: x[0])]
        new_block = build_column_block([blocks_dict[id] for id in sorted_ids])
        column_blocks.append(new_block)
        block_ids -= set(sorted_ids)
    return column_blocks


def main(input_file):
    input_blocks = open(input_file).read().split("\n\n")
    blocks_dict = {i: Block(block) for i, block in enumerate(input_blocks)}

    top_left_corner, bot_left_corner, left_edges = identify_relevant_blocks(blocks_dict)
    for left_edge_candidates in itertools.permutations(left_edges):
        first_col = [top_left_corner, *left_edge_candidates, bot_left_corner]
        try:
            column_blocks = build_columns(blocks_dict, first_col)
            final_block = build_row_block(column_blocks)
            x, y = final_block.get_treasure_coordinates()
            return x * y
        except:
            print(f"Failed with {first_col}")
            continue
    return None


# Remove the last trailing line from puzzle_input to main it works
print(main("input.txt"))
