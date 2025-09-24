def duplicate(s,i=0):
    if i >= len(s)-1:
        return s[i]
    # recursive case
    if s[i] == s[i+1]:
        return s[i] + "*" + duplicate(s,i+1)
    else:
        return s[i] + duplicate(s,i+1)
    

s = input()
print(duplicate(s))