n = int(input("Enter a number: "))

msf  = float('-inf') 
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    if num > msf:
        msf = num
print(f"The largest number is: {msf}")