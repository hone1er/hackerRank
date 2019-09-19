def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    

@memoize
def get_fib(position):
    if position == 0 or position == 1:
        return position
    else:

        return get_fib(position - 1) + get_fib(position - 2)
    return -1