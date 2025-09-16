n = int(input("Enter a positive number: "))

for i in range(1, n+1):
    print(i, end=", ")
print("Finished printing numbers.")
# This program prints numbers from 1 to n, where n is a positive integer input by the user.

for i in range(2, n+1, 2):
    print(i, end=", ")
print("Finished printing even numbers.")
# This program prints even numbers from 2 to n.
