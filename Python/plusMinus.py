#!/bin/python3

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = len([n for n in arr if n > 0])/len(arr)
    neg = len([n for n in arr if n < 0])/len(arr)
    zero = len([n for n in arr if n == 0])/len(arr)
    result = [pos, neg, zero]
    for i in result:
        print(i)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
