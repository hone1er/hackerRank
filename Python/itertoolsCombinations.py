from itertools import combinations

inp = input().split()
word, num = sorted(inp[0]), int(inp[1])
for i in range(num):
    print("\n".join(["".join(tup) for tup in map(tuple, list(combinations(word, i+1)))])) 