import re
from itertools import permutations, product

import numpy as np
from aocd import get_data

input = get_data(day=19, year=2021).split("\n\n")

MIN_BEACON = 12
ROTATIONS = [
    m
    for perm in permutations([0, 1, 2])
    for signs in product([-1, 1], repeat=3)
    for m in [np.array([[signs[i] * (j == perm[i]) for j in range(3)] for i in range(3)])]
    if np.linalg.det(m) == 1
]
IDENTITY_ROT_ID = next(i for i, R in enumerate(ROTATIONS) if np.array_equal(R, np.identity(3, dtype=int)))


# WRITE YOUR SOLUTION HERE
def parse_input(input_blocks):
    return {
        sid: np.array([tuple(map(int, re.findall(r"(-?\d+)", line))) for line in lines.splitlines()[1:]])
        for sid, lines in enumerate(input_blocks)
    }


def compute_distance_between_beacons(M):
    norms = np.sum(M**2, axis=1)
    dot_products = M @ M.T
    return norms[:, None] + norms[None, :] - 2 * dot_products


def find_matching(A, B):
    # A -> (n, n), B -> (m, m)
    # A[:, None, :, None] -> (n, 1, n, 1)
    # B[None, :, None, :] -> (1, m, 1, m)
    # equality_matrix[i, j, k, l] = (A[i, k] == B[j, l])
    equality_matrix = A[:, None, :, None] == B[None, :, None, :]
    diag_n = np.arange(A.shape[0])
    diag_m = np.arange(B.shape[0])
    equality_matrix[diag_n, :, diag_n, :] = False
    equality_matrix[:, diag_m, :, diag_m] = False
    intersection_counts = np.sum(np.any(equality_matrix, axis=3), axis=2)
    return np.argwhere(intersection_counts >= MIN_BEACON - 1)


def find_scanner_positions(scanners_relative):
    scanners_absolute = {0: ([0, 0, 0], IDENTITY_ROT_ID)}
    distance_matrices = {sid: compute_distance_between_beacons(s) for sid, s in scanners_relative.items()}
    queue = [0]
    processed = set()
    while queue and len(scanners_absolute) < len(scanners_relative):
        base_id = queue.pop()
        if base_id in processed:
            continue
        processed.add(base_id)
        base_scanner = scanners_relative[base_id]
        base_coords, base_rot_id = scanners_absolute[base_id]
        base_R = ROTATIONS[base_rot_id]
        for sid, scanner in scanners_relative.items():
            if sid == base_id:
                continue
            matching_pairs = find_matching(distance_matrices[base_id], distance_matrices[sid])
            if len(matching_pairs) >= MIN_BEACON:
                base_idx, idx = np.array(matching_pairs).T
                s0, s1 = base_scanner[base_idx], scanner[idx]
                for idr, R in enumerate(ROTATIONS):
                    uniques = np.unique(s0 @ base_R - s1 @ R, axis=0)
                    if len(uniques) == 1:
                        scanners_absolute[sid] = ((uniques[0] + np.array(base_coords)).tolist(), idr)
                        queue.append(sid)
                        break
    return scanners_absolute


def solve(lines):
    scanners_relative = parse_input(lines)
    scanners_absolute = find_scanner_positions(scanners_relative)

    beacons = set()
    for sid, (scoord, srot) in scanners_absolute.items():
        R = ROTATIONS[srot]
        for beacon in scanners_relative[sid]:
            beacons.add(tuple((scoord + beacon @ R).tolist()))

    scoords = [scoord for scoord, _ in scanners_absolute.values()]
    max_manhattan = max(
        abs(s0x - s1x) + abs(s0y - s1y) + abs(s0z - s1z)
        for (s0x, s0y, s0z), (s1x, s1y, s1z) in permutations(scoords, 2)
    )
    return len(beacons), max_manhattan


def part_1(lines):
    return solve(lines)[0]


def part_2(lines):
    return solve(lines)[1]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
