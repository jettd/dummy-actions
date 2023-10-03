#!/usr/bin/python3

import random

randnums = [random.randint(1, 100) for _ in range(10)]

with open("random_output.txt", "w") as f:
    for num in randnums:
        f.write(str(num) + '\n')

print("10 random numbers.")

exit (0)


