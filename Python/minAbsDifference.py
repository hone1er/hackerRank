def minimumAbsoluteDifference(arr):
    m = None
    arr = sorted(arr)
    for i in range(len(arr)-1):
        calc = abs(arr[i] - arr[i+1])
        if m is None or m > calc:
            m = calc
    return m