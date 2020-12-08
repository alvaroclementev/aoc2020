"""
Solutions to Day 5 of Advent of Code by Alvaro Clemente
"""
from operator import itemgetter


def parse_input(filename="input.txt"):
    """
    Read a the rows from the input file
    """
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def process_line(line):
    """
    The first 5 bits represent the row, FB as a binary number where F == 1 and B == 0
    The same can be applied to the last 3 elements which should be the column
    """
    line_to_bits = (
        line.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")
    )
    row = int(line_to_bits[:7], base=2)
    col = int(line_to_bits[7:], base=2)
    return row, col


def seat_id(row, col):
    return 8 * row + col


# Parsed input
lines = parse_input("input.txt")

# Solution for #1
ids = [seat_id(*process_line(line)) for line in lines]
print(max(ids))


# Solution for #2
ids = [seat_id(*process_line(line)) for line in lines]
min_id, max_id = min(ids), max(ids)

ids_set = set(ids)
missing_ids = [i for i in range(min_id, max_id) if i not in ids_set]
print(missing_ids)
