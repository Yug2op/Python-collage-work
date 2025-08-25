# Basic for loop over a list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# For loop with range
for i in range(5):
    print(i)

# For loop with range and step
for i in range(0, 10, 2):
    print(i)

# For loop over a string
word = "hello"
for char in word:
    print(char)

# For loop over a dictionary (keys)
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key, my_dict[key])

# For loop over dictionary items
for key, value in my_dict.items():
    print(key, value)

# Nested for loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# For loop with else
for i in range(3):
    print(i)
else:
    print("Loop finished")

# For loop with break
for i in range(5):
    if i == 3:
        break
    print(i)

# For loop with continue
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

# -ve indexing in for loop
for i in range(5, 0, -1):
    print(i)