"""
Solutions to Day 3 of Advent of Code by Alvaro Clemente
"""
from functools import reduce

OPEN = "."
TREE = "#"


def parse_map(filename):
    """
    Parse the map into a list of list of characters
    """
    with open(filename, "r") as f:
        lines = f.readlines()
        parsed_map = [list(line.strip()) for line in lines]
    return parsed_map


def check_strategy(parsed_map, x, y, x_change=3, y_change=1):
    """
    Check a walking strategy
    Returns (is_tree, new_x, new_y) where is_tree is a boolean if the
    """
    rows, cols = len(parsed_map), len(parsed_map[0])

    new_x = (x + x_change) % cols
    new_y = y + y_change
    if new_y >= rows:
        return
    new_square = parsed_map[new_y][new_x]
    return new_square == TREE, new_x, new_y


def solve(parsed_map, x_change=3, y_change=1):
    """
    Apply the solution for a given x_change, y_change
    """
    x, y = 0, 0
    trees = 0
    while True:
        # Check the next square
        result = check_strategy(parsed_map, x, y, x_change=x_change, y_change=y_change)
        if result is None:
            return trees
        else:
            is_tree, x, y = result
            if is_tree:
                trees += 1




# Solution for #1
parsed_map = parse_map("input3.txt")
print(solve(parsed_map))

# Solution for #2
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
strategies = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

trees = [solve(parsed_map, x_change=x, y_change=y) for x, y in strategies]
print(reduce(int.__mul__, trees))
