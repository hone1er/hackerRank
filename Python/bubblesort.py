#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
if a == sorted(a):
    print(f"""Array is sorted in 0 swaps.
First Element: {a[0]}
Last Element: {a[len(a)-1]}""")
else:
    swaps = 0
    for j in range(len(a)):
    
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                swaps += 1
    print(f"""Array is sorted in {swaps} swaps.
First Element: {a[0]}
Last Element: {a[len(a)-1]}""")