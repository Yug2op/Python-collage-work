num = int(input("Enter a number: ")) # Taking input from user
sum = 0
while num > 0: # Loop to extract each digit
    digit = num % 10 # Extracting the last digit
    sum += digit # Adding the digit to sum
    num //= 10 # Removing the last digit from number
print("Sum of digits:", sum) # Printing the sum of digits