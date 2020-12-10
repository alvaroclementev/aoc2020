"""
Solutions to Day 9 of Advent of Code by Alvaro Clemente
"""
from collections import deque
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
nums = parse_input()

# Solution for #1
window = deque(nums[:25], maxlen=25)
for num in nums[25:]:
    # This is not the most efficient
    sums = set(a + b for a, b in combinations(window, 2))
    if num not in sums:
        print(f"The solution is {num}")
        break
    # Update the window
    # NOTE(alvaro): The maxlen will make it so the first element is automatically popped
    window.append(num)

# Solution for #2
invalid = 177777905  # Solution from previous
p1, p2 = 0, 1
total = sum(nums[p1:p2+1])
while True:
    # We will update the total after each iteration to avoid recomputing the sums
    print(f"{p1}, {p2}: {total}")
    if total == invalid:
        break
    elif total < invalid:
        p2 += 1
        total += nums[p2]
    elif total > invalid:
        total -= nums[p1]
        p1 += 1
window = nums[p1:p2+1]
minimum = min(window)
maximum = max(window)
print(f"The solution is {minimum + maximum}")
