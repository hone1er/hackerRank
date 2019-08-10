#!/bin/python3

import math
import os
import random
import re
import sys

""" 7
0 0 1 0 0 1 0
"""
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps = 0
    myIter = iter(range(len(c)-1))
    for i in myIter:
        print(i)
        if i+2 < len(c) and c[i+2] == 0:
            steps += 1
            next(myIter, None)
        elif c[i+1] == 0:
            steps += 1
    return steps
        
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
