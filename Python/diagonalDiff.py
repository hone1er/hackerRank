#!/bin/python3
import os


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    primary = sum([arr[n][n] for n in range(len(arr))])
    secondary = sum([arr[len(arr)-(n+1)][n] for n in range(len(arr))])
    return abs(primary-secondary)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
