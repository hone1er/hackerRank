#!/bin/python3

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    ar = sorted(arr)
    mn = sum(ar[:4])
    mx = sum(ar[-4:])
    print(mn, mx)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
