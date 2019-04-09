#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = "{0:b}".format(n)
    value = 0
    values = []
    for i in binary:
        if i == '1':
            value += 1
        elif i == '0':
            values.append(value)
            value = 0
    print(max(values))
