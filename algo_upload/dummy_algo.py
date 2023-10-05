#!/usr/bin/python3

import random

randnums = [random.randint(1, 1000) for _ in range(11)]

with open("random_output.txt", "w") as f:
    for num in randnums:
        f.write(str(num) + '\n')

print("11 random numbers written to random_output")
exit (0)


