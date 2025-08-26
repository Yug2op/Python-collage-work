def greet(): #function without parameters
    print("Hello, World!")
# greet()

# check if a given number is even or odd
num = int(input("Enter a number: "))
def isEven(num:int): #int is a type hint
    if num&1: 
        return False
    else:
        return True
print(isEven(num))