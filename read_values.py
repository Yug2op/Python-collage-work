my_input = input()
print(my_input, type(my_input)) # input() function takes input from user as string
my_input_int = int(input("Enter an integer: ")) # converting input string to integer (Type Casting)
print(my_input_int, type(my_input_int))

print("You have entered:" + str(my_input_int), type(my_input_int)) # converting integer to string for concatenation
print("You have entered:", my_input_int, type(my_input_int)) # using comma to separate values in print function
