"""
Solutions to Day 6 of Advent of Code by Alvaro Clemente
"""
from collections import Counter


def parse_input(filename="input.txt"):
    """
    The answers for a group are in a block (delimited by empty lines)
    For each group the answers for each person are in a line
    """
    with open(filename, "r") as f:
        text = f.read()
    # Parse the groups
    groups = text.split("\n\n")
    answers = [group.split("\n") for group in groups]
    return answers


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


# Parsed input
answers = parse_input()

# Solution for #1
yeses = 0
for group in answers:
    group_answers = set()
    for answer in group:
        group_answers.update(c for c in answer)
    yeses += len(group_answers)
print(yeses)

# Solution for #2
# We now want to know the ones to wich EVERYONE in the group answered yes
yeses = 0
for group in answers:
    group_answers = Counter()
    for answer in group:
        group_answers.update(c for c in answer)
    # Count the ones to which all did
    all_yeses = [key for key, value in group_answers.items() if value == len(group)]
    yeses += len(all_yeses)
print(yeses)
