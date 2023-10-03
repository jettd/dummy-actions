#!/usr/bin/python3

import random

randnums = [random.randint(1, 1000) for _ in range(10)]

with open("random_output.txt", "w") as f:
    for num in randnums:
        f.write(str(num) + '\n')

print("10 random numbers written to random_output")
exit (0)


