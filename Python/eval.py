n = int(input())
s = set(map(int, input().split()))
m = int(input())
def count(s, m):
    
    for _ in range(m):
        func = input().split()
        if len(func) > 1:
            func, var = func[0], func[1]
        else:
            func = func[0]
            var = ""
        eval(f"s.{func}({var})")
    return sum(s)
print(count(s, m))
