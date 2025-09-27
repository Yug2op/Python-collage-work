from collections import defaultdict,Counter


def is_duplicate(arr):
    freq = defaultdict(int)
    for item in arr:
        freq[item] += 1
        if freq [item] > 1:
            return True
    return False

arr = [1,2,3,4,1,2,1]
print(is_duplicate(arr))

print(Counter(arr)) # make frequency table