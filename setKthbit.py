n =42
k = 4
mask = 1 << k # left shift 1 by k bits gives a number with only kth bit set that is 2^k
print (n | mask)