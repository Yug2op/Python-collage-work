n = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, n+1):
    # Print leading spaces
    for j in range(n-i):
        print("  ", end="")
    
    # Print stars
    for k in range(2*i-1):
        print("* ", end="")
    
    # Move to the next line after each row
    print()
    