def is_anagram(s,t): # time complexity is O(n) and space complexity is O(1)
    fmap_s = [0]*26
    fmap_t = [0]*26
    for ch in s:
        idx = ord(ch) - ord('a')
        fmap_s[idx] += 1
    print(fmap_s)
    for ch in t:
        idx = ord(ch) - ord('a')
        fmap_t[idx] += 1
    print(fmap_t)
    for i in range(26):
        if fmap_s[i] != fmap_t[i]:
            return False
    return True

s = "listen"
t = "silent"

print(is_anagram(s,t))

from collections import Counter # Counter is a dictionary that stores the frequency of each character in a string

print(Counter(s))
print(Counter(t))

print(Counter(s) == Counter(t)) # time complexity is O(n) and space complexity is O(1)