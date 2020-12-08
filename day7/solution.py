"""
Solutions to Day 7 of Advent of Code by Alvaro Clemente
"""
import re


def parse_input(filename="input.txt"):
    """
    The answers for a group are in a block (delimited by empty lines)
    For each group the answers for each person are in a line
    """
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def process_lines(lines):
    """
    The first 5 bits represent the row, FB as a binary number where F == 1 and B == 0
    The same can be applied to the last 3 elements which should be the column
    """
    bags = {}
    for line in lines:
        key, rest = line.split("bags contain ", 1)
        key = key.strip()
        # Parse the bags that are contained by key
        contained = [part.strip() for part in re.split("bags?", rest)]
        if contained[0] == "no other":
            # no others
            contained_dict = {}
        else:
            contained_dict = {}
            for part in contained[:-1]:  # We ignore the last '.'
                # Remove , and .
                cleaned_part = part.replace(",", "").replace(".", "").strip()
                # Parse the number and bag
                n, bag = cleaned_part.split(" ", 1)
                n = int(n)
                bag = bag.strip()
                contained_dict[bag] = n
        bags[key] = contained_dict
    return bags


# Parsed input
lines = parse_input()
bags = process_lines(lines)

# Solution for #1
result_set = set()
candidates = ["shiny gold"]
new_candidates = []
while True:
    for bag, contained in bags.items():
        for cand in candidates:
            if cand in contained:
                result_set.add(bag)
                new_candidates.append(bag)
    if len(new_candidates) == 0:
        break
    candidates = new_candidates.copy()
    new_candidates.clear()
print(len(result_set))

# Solution for #2
def check_candidates(bag):
    """
    Check the bags contained
    """
    total = 1  # We always count itself
    for item, count in bags[bag].items():
        total += count * check_candidates(item)
    return total

print(check_candidates("shiny gold") - 1)  # We don't want to count the shiny itself
