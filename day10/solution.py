"""
Solutions to Day 10 of Advent of Code by Alvaro Clemente
"""
# NOTE(alvaro): This was a very nice problem! (#2 specially)
import math
from collections import Counter
from functools import partial
from itertools import combinations


def parse_input(filename="input.txt"):
    """
    The answers for a group are in a block (delimited by empty lines)
    For each group the answers for each person are in a line
    """
    with open(filename, "r") as f:
        lines = [int(line.strip()) for line in f.readlines()]
    return lines


# Parsed input
adapters = parse_input()

# Solution for #1
def build_diffs(input):
    sorted_input = list(sorted(input))
    diffs = [
        inp2 - inp1
        for inp1, inp2 in zip([0] + sorted_input, sorted_input + [sorted_input[-1] + 3])
    ]
    assert max(diffs) < 4, "There is no chain that uses all of the adapters"
    return diffs


diffs = build_diffs(adapters)
counts = Counter(diffs)
print(counts)
print(counts[1] * counts[3])


# Solution for #2
def count_combinations(inputs):
    """
    Count the number of combinations that arrived to this step with an available diff of
    i
    """
    # This accumulates the number of valid combinations that arrive to a step with a
    # difference of i
    diffs = build_diffs(inputs)
    counts = {i: 0 for i in range(3)}
    for i, diff in enumerate(diffs):
        if i == 0:
            if diff == 1:
                # You use this adapter or skip it (potentially)
                counts[0] = 1
                counts[1] = 1
            elif diff == 2:
                counts[0] = 1
                counts[2] = 1
            else:
                counts[0] = 1
        else:
            prev0, prev1, prev2 = counts[0], counts[1], counts[2]
            # Update the counts
            if diff == 1:
                counts[0] = prev0 + prev1 + prev2
                counts[1] = prev0
                counts[2] = prev1
            elif diff == 2:
                counts[0] = prev0 + prev1
                counts[1] = 0
                counts[2] = prev0
            else:
                counts[0] = prev0
                counts[1] = 0
                counts[2] = 0
    return counts

print(count_combinations(adapters))

# Test
inputs = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
test_diffs = build_diffs(inputs)

print(count_combinations(inputs))
