# find function
s = "the sun rise in the east, the sun sets in west"

print(s.find("sun"))
print(s.find("sun",10)) # find sun after index 10
print(s.find("sun",10,20)) # find sun after index 10 and before index 20
print(s.rfind("sun")) # find sun from right
# startIndex and endIndex are optional

# split function
s = "a b c   d"
print(s)
print(s.split()) # split function splits the string into list
sport = "badminton,football,cricket"
print(sport)
print(sport.split()) 
print(sport.split(","))

# join function
s = ["a","b","c"]
print(s)
print(", ".join(s)) # create a single string by connecting all strings of s with ", "
print("-".join(s)) # create a single string by connecting all strings of s with "-"

# Interpolation
name = "Yugank"
age = 24
print(f"My name is {name} and I am {age} years old")

# String formatting
print("My name is %s and I am %d years old" % (name, age))

# String formatting
print("My name is {name} and I am {age} years old".format(name="Yugank", age=24))
