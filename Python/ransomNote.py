#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine = Counter(magazine)
    for word in note:
        if magazine[word]:
            if magazine[word] > 0:
                magazine[word] -= 1
            else:
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
