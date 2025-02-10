# write python program using built in function to display factorial of a number
# write python program using built in function to display fibonacci serise
# write python program using built in function to check a number is armstrong or not
# write python program using built in function to check a number is perfect or not
# write python program using built in function to display a number in reverse order

#Note:- All inputes should be taken from the user


def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num-1)
    
num = int(input("Enter a number to find its factorial: "))
result = factorial(num)

print(f"Fatorial of {num} is {result}")

