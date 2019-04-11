#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.

def sockMerchant(n, ar):
    emptyDict = {}
    pairs = 0
    for x in ar:
        if x not in emptyDict:
            emptyDict[x] = 1
        else:
            emptyDict[x] += 1
    for key in emptyDict:
        if emptyDict[key] >= 2:
            pairs += emptyDict[key]//2
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
