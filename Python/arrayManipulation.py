# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    total = [0 for _ in range(n+1)]
    for i, e in enumerate(queries):
        a = e[0]-1
        b = e[1]
        k = e[2]
        total[a] += k
        total[b] -= k

    maxValue = 0
    runningCount = 0
    for i in total:
        runningCount += i
        if runningCount > maxValue:
            maxValue = runningCount
    return maxValue