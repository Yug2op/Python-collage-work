#Datastructures in python
#List
#create a list
list1 = [1,2,3,'yug',9.65]
print(list1)
#Accessing elements in a list
print(list1[0])
list1.append(10) #add element to the end of the list
print(list1)
list1.insert(2,5) #add element at a specific position
print(list1)
list1.remove(3) #remove element from the list
print(list1)

#Strings
# create a string using double quotes
string1 = "Python programming"
# create a string using single quotes
string1 = 'Python programming'
# create string type variables
name = "Python"
print(name)
message = "I love Python."
print(message)
#Access String Characters in Python
#1. Indexing
message = 'hello'
# access 1st index element
print(message[1]) # "e"
#2. Use of negative index
message = 'hello'
# access 4th last element
print(message[-4]) # "e"
#3.Slicing
message = 'Hello'
# access character from 1st index to 3rd index
print(message[1:4])  # "ell"

#Strings are immutable
message = 'Hello Everyone'
# message[0] = 'M' can`t modify it throw error

# print(message)  
#We can use variable name
message = 'Good Morning'
# assign new string to message variable
message = 'Hello Everyone'
print(message); # prints "Hello Everyone"

# multiline string 
message = """
Basics is very important
It forms the foundation for placement
"""
print(message)

#Operations on string---Compare two strings
str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)


