#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    p1 = 0
    p2 = 0
    for i,j in zip(a,b):
        if i > j:
            p1 += 1
        elif j > i:
            p2 += 1
    return [p1,p2]
