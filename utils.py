import re
import math
from functools import total_ordering


def parse_nums(line, negatives=True):
    num_re = r"-?\d+" if negatives else r"\d+"
    return [int(n) for n in re.findall(num_re, line)]


def factors(n):
    """Returns the factors of n."""
    return sorted(
        x
        for tup in ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)
        for x in tup
    )


def _eratosthenes(n):
    """http://stackoverflow.com/a/3941967/239076"""
    # Initialize list of primes
    _primes = [True] * n

    # Set 0 and 1 to non-prime
    _primes[0] = _primes[1] = False

    for i, is_prime in enumerate(_primes):
        if is_prime:
            yield i

            # Mark factors as non-prime
            for j in xrange(i * i, n, i):  # NOQA
                _primes[j] = False


def primes(n):
    """Return a list of primes from [2, n)"""
    return list(_eratosthenes(n))


class RepeatingSequence:
    def __init__(self, generator, to_hashable=lambda x: x):
        """
        generator should yield the things in the sequence.
        to_hashable should be used if things aren't nicely hashable.
        """
        self.index_to_result = []
        self.hashable_to_index = dict()
        for i, result in enumerate(generator):
            self.index_to_result.append(result)
            hashable = to_hashable(result)
            if hashable in self.hashable_to_index:
                break
            else:
                self.hashable_to_index[hashable] = i
        else:
            raise Exception("generator terminated without repeat")
        self.cycle_begin = self.hashable_to_index[hashable]
        self.cycle_end = i
        self.cycle_length = self.cycle_end - self.cycle_begin

        self.first_repeated_result = self.index_to_result[self.cycle_begin]
        self.second_repeated_result = self.index_to_result[self.cycle_end]

    def cycle_number(self, index):
        """
        Returns which 0-indexed cycle index appears in.
        cycle_number(cycle_begin) is the first index to return 0,
        cycle_number(cycle_end)   is the first index to return 1,
        and so on.
        """
        if index < self.cycle_begin:
            print("WARNING: Index is before cycle!!")
            return 0
        return (index - self.cycle_begin) // self.cycle_length

    def __getitem__(self, index):
        """
        Gets an item in the sequence.
        If index >= cycle_length, returns the items from the first occurrence
        of the cycle.
        Use first_repeated_result and second_repeated_result if needed.
        """
        if index < 0:
            raise Exception("index can't be negative")
        if index < self.cycle_begin:
            return self.index_to_result[index]
        cycle_offset = (index - self.cycle_begin) % self.cycle_length
        return self.index_to_result[self.cycle_begin + cycle_offset]


GRID_DELTA = [[-1, 0], [1, 0], [0, -1], [0, 1]]
OCT_DELTA = [[1, 1], [-1, -1], [1, -1], [-1, 1]] + GRID_DELTA


def get_neighbours(grid, row, col, deltas, fill=None):
    n, m = len(grid), len(grid[0])
    out = []
    for i, j in deltas:
        p_row, p_col = row + i, col + j
        if 0 <= p_row < n and 0 <= p_col < m:
            out.append(grid[p_row][p_col])
        elif fill is not None:
            out.append(fill)
    return out
