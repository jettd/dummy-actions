#!/usr/bin/python3

import random
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

randnums = [random.randint(arg1, arg2) for _ in range(arg3)]

with open("random_output.txt", "w") as f:
    for num in randnums:
        f.write(str(num) + '\n')

print("2) random numbers written to random_arg_output")
exit (0)


