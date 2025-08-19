import re
from itertools import permutations, product

import numpy as np

from aocd import get_data

input = get_data(day=19, year=2021).split("\n\n")

MIN_BEACON = 12


def _parse_input(input_blocks):
    scanners = {}
    for scanner_id, lines in enumerate(input_blocks):
        scanner_coords = []
        for line in lines.splitlines()[1:]:
            x, y, z = map(int, re.findall(r"(-?\d+)", line))
            scanner_coords.append((x, y, z))
        scanners[scanner_id] = np.array(scanner_coords)
    return scanners


def generate_rotation_matrices():
    """Generate all 24 unique 3D rotation matrices corresponding to cube orientations."""
    rotation_matrices = []

    for perm in permutations([0, 1, 2]):
        for signs in product(*[(-1, 1)] * 3):
            matrix = np.zeros((3, 3), dtype=int)
            for i in range(3):
                matrix[i, perm[i]] = signs[i]
            if np.linalg.det(matrix) == 1:
                rotation_matrices.append(matrix)
    return rotation_matrices


def compute_distance_between_beacons(M):
    norms = np.sum(M**2, axis=1)  # shape (50,)
    dot_products = M @ M.T  # shape (50, 50)
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


def solve(scanners_relative):
    ROTATIONS = generate_rotation_matrices()
    IDENTITY_MATRIX = np.identity(3, dtype=int)
    IDENTITY_ROT_ID = next(
        i for i, R in enumerate(ROTATIONS) if np.array_equal(R, IDENTITY_MATRIX)
    )

    scanners_absolute = {0: ([0, 0, 0], IDENTITY_ROT_ID)}  # 3 is the id for identity
    distance_matrices = {
        sid: compute_distance_between_beacons(s_data)
        for sid, s_data in scanners_relative.items()
    }

    queue = [0]
    processed_scanners = []
    while queue:
        base_scanner_id = queue.pop()
        if base_scanner_id in processed_scanners:
            continue
        processed_scanners.append(base_scanner_id)

        base_scanner = scanners_relative[base_scanner_id]
        base_dist_matrix = distance_matrices[base_scanner_id]
        base_coords, base_rot_id = scanners_absolute[base_scanner_id]
        base_R = ROTATIONS[base_rot_id]

        for scanner_id, scanner in scanners_relative.items():
            if scanner_id == base_scanner_id:
                continue
            matching_pairs = find_matching(
                base_dist_matrix, distance_matrices[scanner_id]
            )
            if len(matching_pairs) >= MIN_BEACON:
                base_idx, idx = np.array(matching_pairs).T
                s0, s1 = base_scanner[base_idx], scanner[idx]
                for idr, R in enumerate(ROTATIONS):
                    uniques = np.unique(s0 @ base_R - s1 @ R, axis=0)
                    if len(uniques) == 1:
                        ref_coords = uniques[0] + np.array(base_coords)
                        scanners_absolute[scanner_id] = (ref_coords.tolist(), idr)
                        queue.append(scanner_id)
    return scanners_absolute


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    ROTATIONS = generate_rotation_matrices()
    scanners_relative = _parse_input(lines)
    scanners_absolute = solve(scanners_relative)

    B = set()
    for sid, (scoord, srot) in scanners_absolute.items():
        R = ROTATIONS[srot]
        for beacon in scanners_relative[sid]:
            beacon_coords = scoord + beacon @ R
            B.add(tuple(beacon_coords.tolist()))

    return len(B)


def part_2(lines):
    scanners_relative = _parse_input(lines)
    scanners_absolute = solve(scanners_relative)

    SCOORD = [scoord for (scoord, _) in scanners_absolute.values()]
    return max(
        (abs(s0x - s1x) + abs(s0y - s1y) + abs(s0z - s1z))
        for (s0x, s0y, s0z), (s1x, s1y, s1z) in product(SCOORD, repeat=2)
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
