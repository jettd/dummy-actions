#!/usr/bin/python3

import random
import sys

# Ensure enough arguments are provided
if len(sys.argv) < 4:
    print("Usage: script.py <lower_bound> <upper_bound> <count>")
    exit(1)

# Convert arguments to integers
try:
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    arg3 = int(sys.argv[3])
except ValueError:
    print("All arguments must be integers.")
    exit(1)

# Ensure lower_bound is less than or equal to upper_bound
if arg1 > arg2:
    print("Lower bound must be less than or equal to upper bound.")
    exit(1)

randnums = [random.randint(arg1, arg2) for _ in range(arg3)]

with open("random_output.txt", "w") as f:
    for num in randnums:
        f.write(str(num) + '\n')

print(f"{arg3} random numbers written to random_output.txt")
exit(0)
