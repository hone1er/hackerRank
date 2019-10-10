#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s2 = {letter: idx for idx, letter in enumerate(s2)}
    for letter in s1:
        if letter in s2:
            return "YES"
    return "NO"

# This solution is O(M + N) because it iterates once through each string. 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
