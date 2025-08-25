a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(f"{a} is the largest number") 
else:
    if b>c:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")
# Using nested if-else