#!/bin/python3

import sys

results = []
Q = int(input().strip())
for a0 in range(Q):
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]

    if c % 2 == 1 and r % 2 == 1:
        results.append('black')
    elif c % 2 == 1 and r % 2 == 0:
        results.append('red')
    elif c % 2 == 0 and r % 2 == 1:
        results.append('red')
    elif c % 2 == 0 and r % 2 == 0:
        results.append('black')
print('\n'.join(results))