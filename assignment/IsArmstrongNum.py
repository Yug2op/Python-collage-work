def isArmstrong(num):
    num = str(num)
    n = len(num)
    sum = 0
    for digit in num:
        sum += int(digit) ** n
    return sum == int(num)  
try:
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        print("No")
    elif isArmstrong(num):
        print("Yes")
    else:
        print("No")
except ValueError:
    print("Invalid input. Please enter a valid integer.")