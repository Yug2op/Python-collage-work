# def is_palindrome(s): # time complexity is O(n) and space complexity is O(n)
#     if s == s[::-1]:
#         return True
#     return False

def is_palindrome(s): # time complexity is O(n) and space complexity is O(1)
    i = 0
    j = len(s) -1

    while i<j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
    







s = "racecar"
print(is_palindrome(s))