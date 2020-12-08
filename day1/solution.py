"""
Solutions to Day 1 of Advent of Code by Alvaro Clemente
"""
from itertools import combinations

# Parse input
with open("input1.txt", "r") as f:
    lines = f.readlines()
    nums = [int(x.strip()) for x in lines]


# Solution for #1
for a, b in combinations(nums, 2):
    if a + b == 2020:
        print(f"Solution combination is {a} + {b} = 2020 -> solution is {a * b}")

# Solution for #2
for a, b, c in combinations(nums, 3):
    if a + b + c == 2020:
        print(f"Solution combination is {a} + {b} + {c} = 2020 -> solution is {a * b * c}")
