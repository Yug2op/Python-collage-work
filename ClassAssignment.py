# Write python program to impliment class,object,use defined functiin to display factorial of a number.

class Factorial:
    def __init__(self, num):
        self.num = num
    
    def calculate_factorial(self):
        if self.num < 0:
            return "Factorial is not defined for negative numbers"
        elif self.num == 0 or self.num == 1:
            return 1
        else:
            fact = 1
            for i in range(2, self.num + 1):
                fact *= i  # Correct factorial calculation
            return fact

    def display_factorial(self):
        print(f"Factorial of {self.num} is: {self.calculate_factorial()}")

# Creating an object of Factorial class
num = int(input("Enter a number: "))
fact_obj = Factorial(num)

# Displaying the factorial
fact_obj.display_factorial()
