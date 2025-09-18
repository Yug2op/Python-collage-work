s = {1,2,3,4,5,6}

print(s)
s.add(6)
print(s)
s.remove(3)
print(s)
# s.remove(10) key error
s.discard(10) # nothing happen
print(s)

print(2 in s)
print(10 in s)