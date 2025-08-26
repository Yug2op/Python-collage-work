n = int(input("Enter a number: "))
unique = 0
for _ in range(n):
    num = int(input())
    unique = unique ^ num
print("The unique number is:", unique)
    