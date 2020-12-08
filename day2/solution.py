"""
Solutions to Day 2 of Advent of Code by Alvaro Clemente
"""

def parse_line(line):
    """
    Parse a line of the input, which has the following structure
        `min`-`max` `letter`: `password`
    E.g:
        1-4 m: mrfmmbjxr
    """
    head, password = line.strip().split(":", 1)

    # The password is directly extracted
    password = password.strip()

    # Parse the head of the rule
    range, letter = head.split(" ")
    range_parts = range.split("-")
    assert len(range_parts) == 2, "there should be a range of 2 parts"
    min, max = range_parts
    return int(min), int(max), letter, password


# Parse input
with open("input2.txt", "r") as f:
    lines = f.readlines()
    parts = list(map(parse_line, lines))  # Make it a list so that it is not consumed

# Solution for #1
valid = 0
for min, max, letter, password in parts:
    count = password.count(letter)
    if min <= count <= max:
        valid += 1
print(valid)

# Solution for #2
# The parsing is shared, just the meaning of the min, max is changed
valid = 0
for pos, pos2, letter, password in parts:
    first_letter = password[pos-1]
    second_letter = password[pos2-1]
    if ((first_letter == letter and second_letter != letter) or
            (first_letter != letter and second_letter == letter)):
        valid += 1
print(valid)
