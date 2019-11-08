" Find the minimum number of deletions required to make both strings anagrams of each other"
# "a" "a"
# "abcc" "cbaa" {c:0, b:0, a:1}
# "a" "b"
# "nba" "bntr"
# "abc" "bca"


def min_deletions(s1: str, s2: str) -> int:
    counter = {}
    count = 0
    longer_string = s1 if len(s1) >= len(s2) else s2
    shorter_string = s1 if len(s1) < len(s2) else s2

    for letter in longer_string:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
        
    for letter in shorter_string:
        if letter in counter and counter[letter] > 0:
            counter[letter] -= 1
        else:
            count += 1
    return count

print(min_deletions("abcc", "cbaa"))