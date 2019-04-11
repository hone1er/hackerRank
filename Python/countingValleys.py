#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below. Given number of steps taken(n) and
# a string containing 'U' or 'D' to respresent 1 unit change up or down respectively
# find how many valleys were traversed
def countingValleys(n, s):
    U = 1
    D = -1
    elevation = 0
    elevations = []
    valleys = 0
    for l in s:
        if l == "U":
            elevation += 1
            elevations.append(elevation)
        elif l == "D":
            elevation -= 1
            elevations.append(elevation)
    for h in range(len(elevations)):
        if elevations[h] == 0 and elevations[h-1] < 0:
            valleys += 1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
