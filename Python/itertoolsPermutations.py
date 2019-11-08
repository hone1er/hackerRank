from itertools import permutations
inp = input().split() # [String NumberOfLettersForPermutation]
word, num = inp[0], int(inp[1])
tupList = list(map(tuple,list(permutations(sorted(word), r=num))))
print("\n".join(list(''.join(tup) for tup in tupList)))