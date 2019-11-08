from itertools import combinations_with_replacement

inp = input().split()
word, num = sorted(inp[0]), int(inp[1])

print("\n".join(["".join(tup) for tup in map(tuple, list(combinations_with_replacement(word, num)))]))