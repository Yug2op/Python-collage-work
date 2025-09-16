P = int(input("Enter the Principal amount: ")) # Principal amount
R = int(input("Enter the Rate of interest: ")) # Rate of interest
T = int(input("Enter the Time in years: ")) # Time in years
SI = (P * R * T) / 100 # Simple Interest formula, no need of brackets for mul and division as both have equal precedence and are evaluated left to right
print("The Simple Interest is:", SI) # Displaying the Simple Interest