# Question:- Write a menu driven program to implement atleast 5 built in functions of tuple
def display_menu():
    print("Menu:")
    print("1. Find length of tuple")
    print("2. Find maximum value in tuple")
    print("3. Find minimum value in tuple")
    print("4. Count an element in tuple")
    print("5. Find index of an element in tuple")
    print("6. Exit")

def main():
    tuplee = (1, 2, 3, 4, 5, 6, 2, 3)

    while True:
        display_menu()
        choice = input("Enter your choice from (1-6): ")

        if choice == "1":
            print("Length of tuple:", len(tuplee))

        elif choice == "2":
            print("Maximum value in tuple:", max(tuplee))

        elif choice == "3":
            print("Minimum value in tuple:", min(tuplee))

        elif choice == "4":
            element = int(input("Enter the number to count: "))
            print(f"Count of {element} in tuple:", tuplee.count(element))

        elif choice == "5":
            element = int(input("Enter the number to find index: "))
            print(f"Index of {element} in tuple:", tuplee.index(element))

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()
