from collections import Counter

def minAnagram(s1, s2):
    ''' s1 = string
        s2 = string
        return int minimum number of deletions to create anagram
    '''
    longer_string = s1 if len(s1) >= len(s2) else s2
    shorter_string = s2 if len(s2) <= len(s1) else s1
    s = Counter(longer_string)
    count = 0
    for letter in shorter_string:
        if letter in s and s[letter] > 0:
            s[letter] -= 1
            count += 1
    return len(s1) + len(s2) - (count * 2)



s1 = "abcd"
s2 = "abcd"
print(minAnagram(s1, s2)) # should print 0

s1 = "gbcj"
s2 = "abyd"
print(minAnagram(s1, s2)) # should print 6


s1 = "abc"
s2 = "abcd"
print(minAnagram(s1, s2)) # should print 1

s1 = "abcd"
s2 = "rcd"
print(minAnagram(s1, s2)) # should print 5